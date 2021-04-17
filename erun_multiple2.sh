
# TODO (highlight): steps to use
#   0.  EPaxos has some bugs (see below), if you are not sure whether this is
#       the script's problem (misconfiguration) or EPaxos's problem,
#       start with some small parameters, if that runs, it could be EPaxos's
#   1.  start one or more virtual machines as servers and clients
#       install project RC (Multi-BC) as described in README.md on each VM
#   2.  in your computer or the master VM (see below),
#       configure ServerIps, ClientIps, and MasterIp:
#   2.1 e.g., 1 VM, run all servers and clients there:
#       ServerIps=(<VM-ip>)
#       ClientIps=(<VM-ip>)
#       MasterIp=VM-ip
#   2.2 e.g. 6 VMs. 3 * server VMs + 3 * client VMs
#       ServerIps=(<server-ip1> <server-ip2> <server-ip3>)
#       ClientIps=(<client-ip1> <client-ip2> <client-ip3>)
#       MasterIp=<server-ip1>
#   3.  configure NumOfServerInstances, NumOfClientInstances
#       server instance i will be instantiated to (i % len(ServerIps))-th server VM
#       client instance j will be instantiated to (j % len(ClientIps))-th client VM
#   3.1 e.g. if len(ServerIps) = 3, NumOfServerInstances = 7,
#       server instance 1, 4, 7 will be on <server-ip1>
#       server instance 2, 5 will be on <server-ip2>
#       server instance 3, 6 will be on <server-ip3>
#   3.2 e.g. if len(ServerIps) = 2, NumOfServerInstances = 1,
#       client instance 1 will be on <client-ip1>
#       <client-ip2> will have no instance
#   4.  configure common parameters
#   4.1 configure client parameters reqsNb, writes, conflicts,
#       the explanations and other options are here:
#           https://github.com/efficient/epaxos/blob/master/src/client/client.go#L19
#       to change master and server parameters or add client parameters,
#       locate three TODOs below in the code, and modify them inline:
#           master parameters: https://github.com/efficient/epaxos/blob/master/src/master/master.go#L16
#           server parameters: https://github.com/efficient/epaxos/blob/master/src/server/server.go#L22
#   4.2 configure open-loop or closed-loop:
#       if closed-loop, UNCOMMENT:
#           clientBatchSize=<an integer you want>
#           rounds=$((reqsNb / clientBatchSize))
#       and COMMENT out "round=1"
#       if open-loop, COMMENT out:
#           clientBatchSize=<an integer you want>
#           rounds=$((reqsNb / clientBatchSize))
#       and UNCOMMENT "round=1"
#   5.  for parameters with comments below, adjust them when only necessary -- highly unlikely
#   6.  upload the script to all servers and clients
#       I use Goland's auto-deployment feature to automatically upload the file to all VMs from my Mac
#       see this chapter: https://www.jetbrains.com/help/go/deploying-applications.html
#       and https://github.com/haochenpan/mininet-mgmt#local-environment-for-idea-streamline-uploading
#   7.  you may want to try manual ssh would work with the key downloaded by the RC project
#       at master VM, go to the "RC/aux" folder, and do ssh -i id_rsa root@<some-VM-ip>
#   8.  in "RC/aux/epaxos" folder, run . epaxos.sh to start servers and clients
#       if the experiment is long, type SSHCheckClientProgress on the command line to check whether all clients are finished
#       note: you need to run epaxos.sh once to load the function into your current shell
#   9.  when all clients are finished, run EpKillAll on the command line to kill all servers and the master
#   10. run DownloadLogs to download client logs from client VMs to the master VM,
#       and run Analysis to visually inspect log files and see the throughput and latency report
#   11. run RemoveLogs to clear logs in the master's folder and clients' folders
#   12. update parameters, upload to all servers, and run . epaxos.sh to start a new experiment
#       note: if you have changed the parameters, simply calling Main will not work

# TODO(highlight) Known Issues
#   1.  messages like "rpc.Register: method "ConnectToPeers" -> I simply ignore them
#   2. "listen error:listen tcp :8071: bind: address already in use" -> master port is blocking,
#       maybe you have a running master and have not closed it?
#   3. "Error when reading: EOF" -> clients and servers are not successfully connected
#       kill all instances and add more wait time in the "runServersAndClientsAllMachines" function
#   4. "panic: runtime error: index out of range [5] with length 5" ->
#       to allow more than 5 servers, say 10 servers, do the following changes:
#       1.  in epaxos/src/epaxos/epaxos.go
#               change const DS = 5 to const DS = 10
#               change two occurrences of int32{-1, -1, -1, -1, -1} to int32{-1, -1, -1, -1, -1,-1, -1, -1, -1, -1}
#       2.  in epaxos/src/epaxosproto/epaxosproto.go
#               change all occurrences of [5]int32 to [10]int32
#       4.  recompile the project (in the epaoxs folder)
#               export GOPATH="${GOPATH}":~/epaxos
#               go install master
#               go install server
#               go install client
#        note:  to do this efficiently, you can clone the epaxos project to your personal computer, make these changes
#               and then upload the epaxos folder to the cluster
#   5. "ssh_exchange_identification: Connection closed by remote host" and
#       "ssh_exchange_identification: read: Connection reset by peer" ->
#       SSH script is wrecked. sometimes SSH just retry itself non-stopped so that exceeds
#       the max. # of connects allowed. Use ps -fe | grep ssh in the terminal to see whether that is the issue.
#       This problem occurred when I had the content of kill.sh in this script and tried to call it in the same way
#       I start all servers and clients. When I migrate it out, everything works, but I still don't know why.

# TODO(highlight) Design Choices
#   1.  I separated kill.sh out because of the 5th issue above
#   2.  Instead of using SSH to directly start each server, this script only needs to SSH to a server at most twice
#       (once for starting all servers that one the VM and once for all clients).
#       If the script does SSH too often, e.g., run 20 server instances on one VM so one may need to SSH 20 times,
#       then, some weird things could happen, like the 5th issue above.
#   3.  this script requires root access, since the installation script requires so...


#ServerIps=(10.142.0.57 10.142.0.59 10.142.0.67 10.142.0.68 10.142.0.69 10.142.0.75 10.142.0.76 10.142.0.77 10.142.0.78 10.142.0.79 10.142.0.80 10.142.0.81 10.142.0.82 10.142.0.83 10.142.0.84 10.142.0.60 10.142.0.93 10.142.0.90 10.142.0.88) # 19
#ServerIps=(10.142.0.57 10.142.0.59 10.142.0.67 10.142.0.68 10.142.0.69 10.142.0.75 10.142.0.76 10.142.0.77 10.142.0.78 10.142.0.79 10.142.0.80 10.142.0.81 10.142.0.82 10.142.0.83 10.142.0.84 10.142.0.60 10.142.0.93) # 17
#ServerIps=(10.142.0.57 10.142.0.59 10.142.0.67 10.142.0.68 10.142.0.69 10.142.0.75 10.142.0.76 10.142.0.77 10.142.0.78 10.142.0.79 10.142.0.80 10.142.0.81 10.142.0.82) # 13
#ServerIps=(10.142.0.57 10.142.0.59 10.142.0.67 10.142.0.68 10.142.0.69 10.142.0.75 10.142.0.76 10.142.0.77 10.142.0.78 10.142.0.79 10.142.0.80) # 11
#ServerIps=(10.142.0.57 10.142.0.59 10.142.0.67 10.142.0.68 10.142.0.69 10.142.0.75 10.142.0.76 10.142.0.77 10.142.0.78) # 9
#ServerIps=(10.142.0.57 10.142.0.59 10.142.0.67 10.142.0.68 10.142.0.69 10.142.0.75 10.142.0.76) # 7
#ServerIps=(10.142.0.57 10.142.0.59 10.142.0.67 10.142.0.68 10.142.0.69) # 5
ServerIps=(10.10.1.1 10.10.1.2 10.10.1.3) # 3
#ClientIps=(10.142.0.70 10.142.0.71 10.142.0.72 10.142.0.73 10.142.0.74)
ClientIps=(10.10.1.4 10.10.1.5)
#ClientIps=(10.142.0.70)
MasterIp=10.10.1.1
FirstServerPort=17070 # change it when only necessary (i.e., firewall blocking, port in use)
NumOfServerInstances=3 # before recompiling, try no more than 5 servers. See Known Issue # 4
NumOfClientInstances=100
reqsNb=10000
writes=50
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
ScriptFolder=$EPaxosFolder # where this script, analysis_paxos.py, kill.sh, and py2TimeTool.py are located
LogFolder=$EPaxosFolder/logs
log_file_path_head=${EPaxosFolder}/logs/NS${NS}-NC${NC}-re${reqsNb}-cb${clientBatchSize}-wr${writes}-cf${conflicts}-sp${2}-cp${1}-th${thrifty}

function prepareRun() {
    for ip in "${ServerIps[@]}"
    do
        ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "mkdir -p ${LogFolder}; rm -rf ${LogFolder}/*; cd ${ScriptFolder} && chmod 777 erun_multiple2.sh" 2>&1
        sleep 0.3
    done
    for ip in "${ClientIps[@]}"
    do
        ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "mkdir -p ${LogFolder}; rm -rf ${LogFolder}/*; cd ${ScriptFolder} && chmod 777 erun_multiple2.sh" 2>&1
        sleep 0.3
    done
    wait
}

function runMaster() {
    "${EPaxosFolder}"/bin/emaster -N ${NumOfServerInstances} > ${LogFolder}-master.out 2>&1 & # TODO(highlight): change master parameters here
}

function runServersOneMachine() {
    for idx in $(seq 0 $(($NumOfServerInstances - 1)))
    do
        svrIpIdx=$((idx % ${#ServerIps[@]}))
        svrIp=${ServerIps[svrIpIdx]}
        svrPort=$((FirstServerPort + $idx))
        if [[ ${svrIpIdx} -eq ${EPMachineIdx} ]]
        then
            "${EPaxosFolder}"/bin/eserver -port ${svrPort} -maddr ${MasterIp} -addr ${svrIp} -p 4 -thrifty=true -e=true 2>&1 & # TODO: change server parameters here
#            "${EPaxosFolder}"/bin/server -port ${svrPort} -maddr ${MasterIp} -addr ${svrIp}  -p 4 -thrifty=true 2>&1 & # TODO: change server parameters here
        fi
    done
}

function runClientsOneMachine() {
    mkdir -p ${LogFolder}
    for idx in $(seq 0 $((NumOfClientInstances - 1)))
    do
        cliIpIdx=$((idx % ${#ClientIps[@]}))
        cliIp=${ClientIps[cliIpIdx]}
        if [[ ${cliIpIdx} -eq ${EPMachineIdx} ]]
        then
            "${EPaxosFolder}"/bin/eclient -maddr ${MasterIp} -q ${reqsNb} -w ${writes} -r ${rounds} -p 30 -c ${conflicts} > ${LogFolder}/S${NumOfServerInstances}-C${NumOfClientInstances}-q${reqsNb}-w${writes}-r${rounds}-c${conflicts}--client${idx}.out 2>&1 & # TODO: change client parameters here
        fi
    done
}

function runServersAllMachines() {
    runMaster
    sleep 2

    MachineIdx=0
    for ip in "${ServerIps[@]}"
    do
        ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "cd ${ScriptFolder} && EPScriptOption=StartServers EPMachineIdx=${MachineIdx} /bin/bash erun_multiple2.sh" > ${log_file_path_head}-server$(($i - 1)).out 2>&1 &
        sleep 0.3
        ((MachineIdx++))
    done
}

function runClientsAllMachines() {
    MachineIdx=0
    for ip in "${ClientIps[@]}"
    do
        ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "cd ${ScriptFolder} && EPScriptOption=StartClients EPMachineIdx=${MachineIdx} /bin/bash erun_multiple2.sh" > ${LogFolder}-client$(($MachineIdx - 1)).out 2>&1 &
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
    # send the EPaxos folder to the cluster to propagate the change
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
        ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "ps -fe | grep bin/eclient" 2>&1 &
    done
}

function EpKillAll() {
    for ip in "${ServerIps[@]}"
    do
        ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "cd ${ScriptFolder} && chmod 777 kill.sh && /bin/bash kill.sh" 2>&1 &
        sleep 0.3
    done
    for ip in "${ClientIps[@]}"
    do
        ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "cd ${ScriptFolder} && chmod 777 kill.sh && /bin/bash kill.sh" 2>&1 &
        sleep 0.3
    done
    wait
}

function DownloadLogs() {
#    mkdir -p ${LogFolder}

    for ip in "${ClientIps[@]}"
    do
        scp -o StrictHostKeyChecking=no -r ${SSHKey} root@"$ip" : ${LogFolder}/* ${LogFolder} 2>&1 &
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


remove_logs() {
    for ip in "${ServerIps[@]}"; do
        ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"${ip}" "rm -rf ${LogFolder}" &
    done
    for ip in "${ClientIps[@]}"; do
        ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"${ip}" "rm -rf ${LogFolder}" &
    done
    wait
}

#remove_logs
prepareRun
wait
Main
wait
#SSHCheckClientProgress
#DownloadLogs
wait
EpKillAll
