source ./profile.sh

function kill(){
  for ip in "${ServerIps[@]}"
  do
    ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "cd ${EPaxosFolder} && . kill.sh" 2>&1
  done
  for ip in "${ClientIps[@]}"
  do
    ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "cd ${EPaxosFolder} && . kill.sh" 2>&1
  done
}

kill