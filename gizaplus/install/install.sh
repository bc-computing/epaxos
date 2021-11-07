# Make sure shell code is run inside the directory
source ../base-profile.sh

function install_key() {
    mkdir -p ~/.ssh/
    cat "${EPaxosFolder}"/run_abd/id_rsa.pub >>~/.ssh/authorized_keys # public key is stored in .ssh folder to accept ssh connections
    chmod 400 "${SSHKey}" # private key is readable to connect to other nodes with corresponding public key
}

# Installs a version of Python, which is used by the analysis program
function install_python() {
    sudo apt update
    sudo apt install -y gcc
    sudo apt install -y software-properties-common
    sudo add-apt-repository -y ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install -y ${py_ver}
    ${py_ver} --version
}

function install_go() {
    wget -q https://golang.org/dl/${go_tar}
    sudo tar -C /usr/local -xzf ${go_tar}
    rm ${go_tar}
    echo 'export PATH=${PATH}:/usr/local/go/bin' >>~/.bashrc
    echo 'export GOPATH=~/go' >>~/.bashrc
    echo 'export GO111MODULE="auto"' >>~/.bashrc
    source ~/.bashrc
    go version
}

install_key
install_go