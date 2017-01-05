# Mini analysis with CMS data

The goal will be to study and analyse simulation data and real data from CMS in the context of the HZZ4l analysis. This study will be done in Python with the [ROOT library](https://root.cern.ch/) and [Jupyter notebooks](http://jupyter.org/).

## First steps
Connect with ssh to the polui03 machine:
```bash
ssh -Y USERNAME@polui03.in2p3.fr
```
Install and initialize the working area:
```bash
git clone https://github.com/LLRCMS/MiniStage.git MiniStage
cd MiniStage
source setup_env.sh
./init.py
```
The last command will for ask a port number to connect to the Jupyter notebook. It can be for instance any number between 8000 and 9000. It will then ask for a password that will be used to connect to the notebook.  
Launch the Jupyter server:
```bash
./launch_notebook.sh
```
To connect to the server from a local computer, the server port needs to be forwarded through ssh. On Linux machines this can be done with the following lines in `.ssh/config`:
```
Host jupyter
  Hostname polui03.in2p3.fr
  User YOUR_USER_NAME
  LocalForward CHOSEN_PORT localhost:CHOSEN_PORT
```
And connect to the host `jupyter`:
```bash
ssh jupyter
```
Finally, connect to `http://localhost:CHOSEN_PORT` from your favorite browser.

Next time, once eveything is already initialized, the steps are:
```bash
# On polui03
cd MiniStage
source setup_env.sh
./launch_notebook.sh
# On a local machine
ssh jupyter
```
