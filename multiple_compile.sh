source ./profile.sh

function compile(){
  for ip in "${ServerIps[@]}"
  do
    ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "cd ${EPaxosFolder} && . compile.sh" 2>&1
  done
  for ip in "${ClientIps[@]}"
  do
    ssh -o StrictHostKeyChecking=no -i ${SSHKey} root@"$ip" "cd ${EPaxosFolder} && . compile.sh" 2>&1
  done
}

compile