NumOfClientInstances=15

ServerIps=(10.142.15.206 10.142.0.28 10.142.0.95) # 3-same zone
ServerIps=(10.142.15.206 10.142.0.45 10.142.0.91) # 3-diff zone
ClientIps=(10.142.15.203 10.142.0.7 10.142.0.9)
MasterIp=10.142.15.206

TypeEp=false
NumOfServerInstances=3 

# if closed-loop, uncomment two lines below
#clientBatchSize=10
#rounds=$((reqsNb / clientBatchSize))
# if open-loop, uncomment the line below
rounds=1 # open-loop

FirstServerPort=17070
reqsNb=10000
writes=50
dlog=false
conflicts=0
thrifty=false



# some constants
SSHKey=/root/go/src/rc3/deployment/install/id_rsa # RC project has it
EPaxosFolder=/root/go/src/epaxos # where the epaxos' bin folder is located
LogFolder=/root/go/src/epaxos/logs

function prepareRun() {
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

function runMaster() {
    "${EPaxosFolder}"/bin/master -N ${NumOfServerInstances} 2>&1 &
}

function runServersOneMachine() {
    for idx in $(seq 0 $(($NumOfServerInstances - 1)))
    do
        svrIpIdx=$((idx % ${#ServerIps[@]}))
        svrIp=${ServerIps[svrIpIdx]}
        svrPort=$((FirstServerPort + $idx))
        if [[ ${svrIpIdx} -eq ${EPMachineIdx} ]]
        then
            "${EPaxosFolder}"/bin/server -port ${svrPort} -maddr ${MasterIp} -addr ${svrIp} -p 4 -thrifty=${thrifty} -e=${TypeEp} 2>&1 &
        fi
    done
}

function runClientsOneMachine() {
    ulimit -n 65536
    mkdir -p ${LogFolder}
    for idx in $(seq 0 $((NumOfClientInstances - 1)))
    do
        cliIpIdx=$((idx % ${#ClientIps[@]}))
        cliIp=${ClientIps[cliIpIdx]}
        if [[ ${cliIpIdx} -eq ${EPMachineIdx} ]]
        then
            "${EPaxosFolder}"/bin/client -maddr ${MasterIp} -q ${reqsNb} -w ${writes} -r ${rounds} -e=${TypeEp} -p 30 -c ${conflicts} > ${LogFolder}/S${NumOfServerInstances}-C${NumOfClientInstances}-q${reqsNb}-w${writes}-r${rounds}-c${conflicts}--client${idx}.out 2>&1 &
        fi
    done
}

function runServersAllMachines() {
    runMaster
    sleep 2

    MachineIdx=0
    for ip in "${ServerIps[@]}"
    do
        ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "cd ${EPaxosFolder} && EPScriptOption=StartServers EPMachineIdx=${MachineIdx} /bin/bash epaxos.sh" 2>&1 &
        sleep 0.3
        ((MachineIdx++))
    done
}

function runClientsAllMachines() {
    MachineIdx=0
    for ip in "${ClientIps[@]}"
    do
        ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "cd ${EPaxosFolder} && EPScriptOption=StartClients EPMachineIdx=${MachineIdx} /bin/bash epaxos.sh" 2>&1 &
        sleep 0.3
        ((MachineIdx++))
    done
}

function runServersAndClientsAllMachines() {
    runServersAllMachines
    sleep 5 # TODO(highlight): add wait time here
    runClientsAllMachines
}

function SendEPaxosFolder() {
    for ip in "${ServerIps[@]}"
    do
        scp -o StrictHostKeyChecking=no -i ${SSHKey} -r ${EPaxosFolder} root@"$ip":~  2>&1 &
        sleep 0.3
    done
    for ip in "${ClientIps[@]}"
    do
        scp -o StrictHostKeyChecking=no -i ${SSHKey} -r ${EPaxosFolder} root@"$ip":~  2>&1 &
        sleep 0.3
    done
    wait
}

function SSHCheckClientProgress() {
    for ip in "${ClientIps[@]}"
    do
        ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "ps -fe | grep bin/client" 2>&1 &
    done
}

function EpKillAll() {
    for ip in "${ServerIps[@]}"
    do
        ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "cd ${EPaxosFolder} && chmod 777 kill.sh && /bin/bash kill.sh" 2>&1 &
        sleep 0.3
    done
    for ip in "${ClientIps[@]}"
    do
        ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "cd ${EPaxosFolder} && chmod 777 kill.sh && /bin/bash kill.sh" 2>&1 &
        sleep 0.3
    done
    wait
}

function DownloadLogs() {
    mkdir -p ${LogFolder}

#    for ip in "${ServerIps[@]}"
#    do
#        scp -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip":${LogFolder}/*.out ${LogFolder} 2>&1 &
#        sleep 0.3
#    done

    for ip in "${ClientIps[@]}"
    do
        scp -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip":${LogFolder}/*.out ${LogFolder} 2>&1 &
        sleep 0.3
    done
}

function RemoveLogs(){
  for ip in "${ClientIps[@]}"
  do
        ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "rm -rf ${LogFolder}/*" 2>&1 &
        sleep 0.3
  done

  for ip in "${ServerIps[@]}"
  do
        ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "rm -rf ${LogFolder}/*" 2>&1 &
        sleep 0.3
  done
}

function Analysis() {
    sleep 3
#    cat ${LogFolder}/*.out  # for visual inspection
    python3.8 analysis_paxos.py ${LogFolder} print-title
}

function Main() {
    case ${EPScriptOption} in
        "StartServers")
            runServersOneMachine
            ;;
        "StartClients")
            runClientsOneMachine
            ;;
        "killall")
            EpKillAll
            ;;
        *)
            runServersAndClientsAllMachines
            ;;
    esac
}

#SendEPaxosFolder
#prepareRun;
RemoveLogs
wait
Main
wait
DownloadLogs
wait
EpKillAll
