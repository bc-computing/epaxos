ServerIps=(10.10.1.1 10.10.1.2 10.10.1.3)
ClientIps=(10.10.1.4 10.10.1.5)
EPaxosFolder=~/go/src/epaxos


kill_all(){
  for ip in "${ServerIps[@]}"; do
    echo "${ip}"
    if [ $ip -eq ${ServerIps[0]} ]; then
      echo "Killing Master Server ${ip}"
      . ekill.sh
    else
      ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" ". ${EPaxosFolder}/ekill.sh"
    fi
  done
  for ip in "${ClientIps[@]}"; do
    ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" ". ${EPaxosFolder}/ekill.sh"
  done
}

kill_all