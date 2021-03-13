# 1. configurations
NS=5 # the number of servers
NC=10 # the number of clients
mport=17070
maddr=localhost
reqsNb=100000
cbatch=10
writes=50
rounds=$(($reqsNb / $cbatch))
serverP=2
clientP=1
conflicts=0

# 2. runtime variables (no need to modify)
efolder=${HOME}/go/src/epaxos
mkdir -p ${efolder}/logs
servers=() # server PIDs
clients=() # client PIDs

# 3. start EPaxos leader
emaster -port=$mport -N=$NS \
    >${efolder}/logs/NS${NS}-NC${NC}-q${reqsNb}-w${writes}-r${rounds}-sp${serverP}-cp${clientP}-c${conflicts}-master.out 2>&1 &
servers[0]=$!
echo "master started"
sleep 1

# 4. start EPaxos servers
for i in $(seq $NS); do
    eserver -port=$(($mport + $i)) -maddr=$maddr -mport=$mport -addr=localhost -e=true -p=$serverP -thrifty=true \
        >${efolder}/logs/NS${NS}-NC${NC}-q${reqsNb}-w${writes}-r${rounds}-sp${serverP}-cp${clientP}-c${conflicts}-server$(($i - 1)).out 2>&1 &
    servers[i]=$!
done
echo "servers started"
sleep 3

# 5. start EPaxos clients
for i in $(seq $NC); do
    eclient -maddr=$maddr -mport=$mport -q=$reqsNb -w=$writes -e=true -r=$rounds -p=$clientP -c=$conflicts \
        >${efolder}/logs/NS${NS}-NC${NC}-q${reqsNb}-w${writes}-r${rounds}-sp${serverP}-cp${clientP}-c${conflicts}-client$(($i - 1)).out 2>&1 &
    clients[$(($i - 1))]=$!
done
echo "clients started"

# prepare nettop monitoring
pids="" # a list of PIDs that will be monitored
for pid in ${servers[*]}; do
    pids=${pids}"-p $pid "
done
for pid in ${clients[*]}; do
    pids=${pids}"-p $pid "
done
echo $pids

# conduct monitoring (on Mac)
nettop -x -P -l 0 -J time,bytes_in,bytes_out ${pids} \
    > ${efolder}/logs/NS${NS}-NC${NC}-q${reqsNb}-w${writes}-r${rounds}-sp${serverP}-cp${clientP}-c${conflicts}-nettop.out 2>&1 &
netPID=$!

# waits the clients to exit
for pid in ${clients[*]}; do
    wait $pid
done

# stop monitoring 
echo "clients exited, wait a few more seconds before stopping nettop (process ${netPID})..."
sleep 5
kill -2 $netPID

for pid in ${servers[*]}; do
    kill -2 $pid
done
