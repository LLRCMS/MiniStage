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
The last command will ask for a port number (e.g. in that case any number between 8000 and 9000) as well as a password used to connect to the Jupyter server.  
Then to launch the Jupyter server, type:
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
And connecting to the host `jupyter`:
```bash
ssh jupyter
```

Next time, once everything is already initialized, the steps are:
```bash
# On polui03
cd MiniStage
source setup_env.sh
./launch_notebook.sh
# On a local machine
ssh jupyter
```

## Editing and running code
Editing and running code is done inside a browser connected to the Jupyter server at the following address:
```
http://localhost:CHOSEN_PORT
```
Click on the `hzz4l_analysis.ipynb` file to open the notebook and start editing code.


