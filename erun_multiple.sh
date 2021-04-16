# Directory Vars
User="$USER"
RCFolder=~/go/src/rc3 # assuming rc4 is installed, this should be path
EPaxosFolder=~/go/src/epaxos # assuming epaxos is installed, this should be path
LogFolder=$EPaxosFolder/logs
BinFolder=$EPaxosFolder/bin
SSHKey=$RCFolder/deployment/install/id_rsa

# Run Specific Vars
ServerIps=(10.10.1.1 10.10.1.2 10.10.1.3)
ClientIps=(10.10.1.4 10.10.1.5)
MasterIp=10.10.1.1
FirstServerPort=17070
NumOfServerInstances=3
NumOfClientInstances=100
ReqsNB=10000
Writes=50
Conflicts=100
# if closed-loop, uncomment two lines below
clientBatchSize=10
rounds=$((ReqsNB / clientBatchSize))
# if open-loop, uncomment the line below
#rounds=1 # open-loop
serverP=2       # server's GOMAXPROCS (sp)
clientP=1       # client's GOMAXPROCS (cp)
thrifty=false   # EPaxos: "Use only as many messages as strictly required for inter-replica communication" (th)



start_servers(){
  for ip in "${ServerIps[@]}"; do
    if [ $ip -eq ${ServerIps[0]} ]; then
      ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "mkdir -p ${LogFolder}; rm -rf ${LogFolder}/*; emaster -port=$FirstServerPort -N=$NumOfServerInstances \>${log_file_path_head}-master.out 2>&1"
    else
      ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "mkdir -p ${LogFolder}; rm -rf ${LogFolder}/*; eserver -port=$(($FirstServerPort + $i)) -maddr=$MasterIp -mport=$FirstServerPort -addr=localhost -e=true -p=$serverP -thrifty=${thrifty} \>${log_file_path_head}-server$(($i - 1)).out 2>&1 &" 2>&1
    fi
  done
}

start_clients(){
  for ip in "${ClientIps[@]}"; do
    ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "mkdir -p ${LogFolder}; rm -rf ${LogFolder}/*; eclient -maddr=$MasterIp -mport=$FirstServerPort -q=$ReqsNB -w=$Writes -e=true -r=$rounds -p=$clientP -c=$Conflicts \>${log_file_path_head}-client$(($i - 1)).out 2>&1 &"
  done
}

remove_logs_and_clear_project_and_compile(){
  for ip in "${ServerIps[@]}"; do
    ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "rm -rf ${LogFolder}/* && rm -rf ${BinFolder} && cd ${EPaxosFolder} && . ecompile.sh && echo 'compiled for ${ip}'"
  done
  for ip in "${ClientIps[@]}"; do
    ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "rm -rf ${LogFolder}/* && rm -rf ${BinFolder} && cd ${EPaxosFolder} && . ecompile.sh && echo 'Compiled for ${ip}'"
  done
}

correct_go(){
  for ip in "${ServerIps[@]}"; do
    ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "export PATH=$PATH:/usr/local/go/bin >> ~/.bashrc && source ~/.bashrc"
  done
  for ip in "${ClientIps[@]}"; do
    ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "export PATH=$PATH:/usr/local/go/bin >> ~/.bashrc && source ~/.bashrc"
  done
}

run_once(){
  correct_go
  remove_logs_and_clear_project_and_compile
  start_servers
  start_clients
}

run_once



