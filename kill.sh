pgrep -af /root/go/src/epaxos/bin/emaster | while read -r pid cmd ; do
     echo "pid: $pid, cmd: $cmd"
    kill -9 $pid > /dev/null 2>&1
done
pgrep -af /root/go/src/epaxos/bin/eserver | while read -r pid cmd ; do
     echo "pid: $pid, cmd: $cmd"
    kill -9 $pid > /dev/null 2>&1
done
pgrep -af /root/go/src/epaxos/bin/eclient | while read -r pid cmd ; do
     echo "pid: $pid, cmd: $cmd"
    kill -9 $pid > /dev/null 2>&1
done