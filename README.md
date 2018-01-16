# Mini analysis with CMS data

The goal will be to study and analyse simulation data and real data from CMS in the context of the HZZ4l analysis. This study will be done in Python with the [ROOT library](https://root.cern.ch/) and [Jupyter notebooks](http://jupyter.org/).  
ROOT is a data analysis library written in C++ and widely used in the HEP community. It is possible to use ROOT in Python as well, which will be done here.  
Jupyter is a web application that allows you to create notebooks containing code, text and data visualizations. You will work with Jupyter notebooks running on LLR machines, where the CMS HZZ4l data are located.  

The following steps describe how to install and initialize your working area on one of the LLR machines, and forward the Jupyter notebook to your computer.  
## First steps
Connect with ssh to the polui03 machine. To do so it is needed to first connect to a gate machine (llrgate02).
```bash
# from your computer
ssh -Y USERNAME@llrgate02.in2p3.fr
# from llrgate02
ssh -Y USERNAME@polui03.in2p3.fr
```
Create a working area, install and initialize the working area:
```bash
# On polui03
mkdir -p ~/PHY584/CMSHZZ/2018/YOURNAME
git clone https://github.com/LLRCMS/MiniStage.git MiniStage
cd MiniStage
source setup_env.sh
./init.py
```
The last command will ask for a port number (e.g. it can be for instance any number between 7000 and 10000) as well as a password used to connect to the Jupyter server. The port number has to be different for each person.

Then to launch the Jupyter server, type:
```bash
# On polui03
./launch_notebook.sh
```
(In case the chosen port is already used it will chose an other random port and the number will be written in the command output.)

To connect to the server from your computer, the server port needs to be forwarded through ssh. On Linux machines this can be done with the following lines in `.ssh/config`:
```
# Lines to be put in .ssh/config on your computer
Host jupyter
  Hostname polui03.in2p3.fr
  User USERNAME
  LocalForward CHOSEN_PORT localhost:CHOSEN_PORT
  ProxyCommand ssh -q USERNAME@llrgate02.in2p3.fr nc %h %p
```
And connecting to the host `jupyter`:
```bash
# On your computer
ssh jupyter
```
Before leaving, shut down the jupyter server with `Ctrl-C` in the terminal where it is running.

Next time, once everything is already initialized, the steps are:
```bash
# On polui03
cd MiniStage
source setup_env.sh
./launch_notebook.sh
# On your computer
ssh jupyter
```

## Editing and running code
Editing and running code is done inside a web browser connected to the Jupyter server at the following address:
```
http://localhost:CHOSEN_PORT
```
Click on the `hzz4l_analysis.ipynb` file to open the notebook and start editing code.


