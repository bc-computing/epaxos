1.SSH into each of the VMs and do the following:
    1. `cd ~/go/src`
        1. ```git clone https://github.com/zhouaea/epaxos.git && cd epaxos```
        3. `git checkout patch-1`
        4. `cd epaxos`
        4. ```. compile.sh```
        5. After compiling, you should see
       </br>
       ```Built Master```
       </br>
       ```Built Server```
       </br>
       ```Built Client```
    2. `cd run_abd`
        1. `. initialize_keys.sh`
        2. `. runABD.sh`