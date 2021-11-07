## Testing ABD on Cloudlab
### Installation(***In Each VM***)
1. SSH into each of the VMs and do the following inside /root:
    1. ```sudo su```
    2. ```cd```
    3. ```mkdir -p go/src && cd go/src```
    4. ```git clone https://github.com/bc-computing/epaxos.git && cd epaxos```
    5. ```git checkout gizaplus```
2. Install go, python, and configure ssh.
   1. ```cd gizaplus/install```
   2. ```. install.sh```
3. Compile go binaries
   1. ```cd ../.. && . compile.sh``` 
   2. After compiling, you should see:
      </br>
      ```Built Master```
      </br>
      ```Built Server```
      </br>
      ```Built Client```


### Configuration(***In Each VM***)
1. Inside ```base-profile.sh``` and ```profileX.sh``` configure:
    1. Run Configs (NClients, etc.)
    2. External/Internal IPs (Depending on zonage)
    3. Paths to your folders/keys. I usually install in ``root``.
2. For further debugging, you may also turn on the ```dlog``` which is the native logging service of Epaxos.
    1. Inside your epaxos folder, ```cd src/dlog && nano dlog.go```
    2. Edit this ```dlog = false```
    3. Make sure you then recompile binaries with, ```. compile.sh```

### Run(***In Controller VM***)
1. Finally, run ```cd gizaplus/run_abd && runABD.sh > run.txt``` in the terminal of your controller vm.
2. If all works correctly, you should see n client logs inside the /logs directory in your controller VM.
3. For throughput/latency analysis, run:
    1. ```cd ../.. && python3.8 analysis.py ./logs```

If something goes wrong, run `. kill.sh` on each machine