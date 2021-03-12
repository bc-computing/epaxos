# assume EPaxos source code has been clone to efolder
efolder=${HOME}/go/src/epaxos
branch=morethan5
profile=${HOME}/.bash_profile # .bash_profile for MacOS but .profile for Ubuntu?

touch ${profile} # create one if profile does not exist

# https://stackoverflow.com/a/1397020
# for go build to work; for running Shell code anywhere; for running EPaxos' binaries anywhere
if [[ ":${GOPATH}:" != *":${efolder}:"* ]]; then
  echo 'export GOPATH=${GOPATH}':"${efolder}" >>${profile}
  source ${profile}
fi
if [[ ":${PATH}:" != *":${efolder}:"* ]]; then
  echo 'export PATH=${PATH}':"${efolder}" >>${profile}
  chmod 777 ${efolder}/*.sh
  source ${profile}
fi
if [[ ":${PATH}:" != *":${efolder}/bin:"* ]]; then
  echo 'export PATH=${PATH}':"${efolder}/bin" >>${profile}
  source ${profile}
fi

cd ${efolder}
git checkout $branch
# # prefix binaries with "e" to indicate they belong to EPaxos
# # https://stackoverflow.com/a/33243591
go build -o ${efolder}/bin/emaster master # emaster -N=3
go build -o ${efolder}/bin/eserver server
go build -o ${efolder}/bin/eclient client
