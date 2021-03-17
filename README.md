[the original readme](original.md)

# What's new
- .gitignore
- ecompile.sh
- erun.sh
- ekill.sh
- eclear.sh
- eanalysis.py: analysis the network usage over time on a single machine

# The workflow
- in this folder, do `. ecompile.sh` to compile the master, server, and client code
- adjust parameters in `erun.sh` and do `. erun.sh` to run EPaxos
- when an EPaxos run is over, run `python3 eanalysis-log.py` to see the throughput
- run `. eclear.sh` to remove logs and those (empty) EPaxos storage files
- If EPaxos goes wrong at any time, run `. ekill.sh` to kill  master, server, and client instances.
