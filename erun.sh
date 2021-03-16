# 1. user configurations
maddr=localhost # EPaxos master address
mport=17070     # EPaxos master port
NS=5            # the number of servers
NC=10            # the number of clients
reqsNb=10000000  # the number of unbatched-requests per client (q)
cbatch=1000      # the number of requests in a client batch (cb)
writes=50       # the percentage of client write operations / read & write operations (w)
conflicts=0     # the percentage fo client read & write conflicts (c)
serverP=2       # server's GOMAXPROCS (sp)
clientP=1       # client's GOMAXPROCS (cp)
thrifty=false   # EPaxos: "Use only as many messages as strictly required for inter-replica communication" (t)

# 2. runtime variables (no need to modify)
rounds=$(($reqsNb / $cbatch)) # the number of rounds = reqsNb / cbatch
efolder=${HOME}/go/src/epaxos
mkdir -p ${efolder}/logs
servers=() # server PIDs
clients=() # client PIDs

# 3. start the EPaxos leader
emaster -port=$mport -N=$NS \
    >${efolder}/logs/NS${NS}-NC${NC}-q${reqsNb}-cb${cbatch}-w${writes}-c${conflicts}-sp${serverP}-cp${clientP}-t${thrifty}-master.out 2>&1 &
servers[0]=$!
echo "master started"
sleep 1

# 4. start EPaxos servers
for i in $(seq $NS); do
    eserver -port=$(($mport + $i)) -maddr=$maddr -mport=$mport -addr=localhost -e=true -p=$serverP -thrifty=${thrifty} \
        >${efolder}/logs/NS${NS}-NC${NC}-q${reqsNb}-cb${cbatch}-w${writes}-c${conflicts}-sp${serverP}-cp${clientP}-t${thrifty}-server$(($i - 1)).out 2>&1 &
    servers[i]=$!
done
echo "servers started"
sleep 3

# 5. start EPaxos clients
for i in $(seq $NC); do
    eclient -maddr=$maddr -mport=$mport -q=$reqsNb -w=$writes -e=true -r=$rounds -p=$clientP -c=$conflicts \
        >${efolder}/logs/NS${NS}-NC${NC}-q${reqsNb}-cb${cbatch}-w${writes}-c${conflicts}-sp${serverP}-cp${clientP}-t${thrifty}-client$(($i - 1)).out 2>&1 &
    clients[$(($i - 1))]=$!
done
echo "clients started"

# 6. prepare nettop monitoring
pids="" # a list of PIDs that will be monitored
for pid in ${servers[*]}; do
    pids=${pids}"-p $pid "
done
for pid in ${clients[*]}; do
    pids=${pids}"-p $pid "
done
# echo $pids

# 7. conduct monitoring (on Mac)
nettop -P -l 0 -J time,bytes_in,bytes_out ${pids} \
    >${efolder}/logs/NS${NS}-NC${NC}-q${reqsNb}-cb${cbatch}-w${writes}-c${conflicts}-sp${serverP}-cp${clientP}-t${thrifty}-nettop.out 2>&1 &
netPID=$!

# 8. waits the clients to exit
for pid in ${clients[*]}; do
    wait $pid
done

# 9. stop monitoring
echo "clients exited, wait a few more seconds before stopping nettop (process ${netPID})..."
sleep 5
kill -2 $netPID

# 10. stop servers and the master
for pid in ${servers[*]}; do
    kill -2 $pid
done
