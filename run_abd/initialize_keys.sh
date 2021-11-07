# Make sure shell code is run inside the directory
source ./base-profile.sh

mkdir -p ~/.ssh/
cat "${EPaxosFolder}"/run_abd/id_rsa.pub >>~/.ssh/authorized_keys
chmod 400 "${EPaxosFolder}"/run_abd/id_rsa