ServerIps=(10.10.1.1 10.10.1.2 10.10.1.3) # 3
#ClientIps=(10.142.0.70 10.142.0.71 10.142.0.72 10.142.0.73 10.142.0.74)
ClientIps=(10.10.1.3 10.10.1.4 10.10.1.5)
#ClientIps=(10.142.0.70)
MasterIp=10.10.1.1
FirstServerPort=17070 # change it when only necessary (i.e., firewall blocking, port in use)
NumOfServerInstances=3 # before recompiling, try no more than 5 servers. See Known Issue # 4
NumOfClientInstances=100
reqsNb=100000
writes=50
dlog=false
conflicts=100
thrifty=false

# if closed-loop, uncomment two lines below
clientBatchSize=10
rounds=$((reqsNb / clientBatchSize))
# if open-loop, uncomment the line below
#rounds=1 # open-loop

# some constants
SSHKey=/root/go/src/rc3/deployment/install/id_rsa # RC project has it
EPaxosFolder=/root/go/src/epaxos # where the epaxos' bin folder is located
LogFolder=/root/go/src/epaxos/logs


prepare_run() {
    for ip in "${ServerIps[@]}"
    do
        ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "mkdir -p ${LogFolder}; rm -rf ${LogFolder}/*; cd ${EPaxosFolder} && chmod 777 epaxos.sh" 2>&1
        sleep 0.3
    done
    for ip in "${ClientIps[@]}"
    do
        ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "mkdir -p ${LogFolder}; rm -rf ${LogFolder}/*; cd ${EPaxosFolder} && chmod 777 epaxos.sh" 2>&1
        sleep 0.3
    done
    wait
}

run_tests(){
  thrifty=true
  conflicts=0
  sh epaxos.sh
  wait
  generate_result
  thrifty=true
  conflicts=100
  sh epaxos.sh
  wait
  thrifty=false
  conflicts=0
  sh epaxos.sh
  wait
  thrifty=false
  conflicts=100
  sh epaxos.sh
  wait
  generate_result
}

generate_result(){
  python3.8 epaxos-analysis.py ./logs > result.txt
  wait
  rm -rf ./logs/*
}

run(){
  prepare_run
  run_tests
}