# How to host Jupyter Notebook on a remote server
---
This blog post intends on teaching the reader the steps to hosting a Jupyter Notebook on a remote server. However, you must first meet some requirements to begin:

1. Obtain SSH credentials to your remote server.
2. Install Jupyter Notebook onto the remote server. (Ask your system admin if you think it is not installed.)
3. Remote VPN into your remote server.

Once these four things are accomplished, you can begin.

*Note*: If you want to edit your Jupyter Notebook without a remote machine, you will have to install [Jupyter Notebook](https://jupyter.org/install) onto your local machine.

---
# Step 1: SSH Tunnelling

To begin, you will need to log into your remote server. To do that in your command terminal, enter the following command. Note, this tutorial is tailored to the University of Memphis's HPC, so all login credintials pertain to their sign in process.

`ssh -Y username@hpclogin.memphis.edu`

The system will ask you to enter your password if you do not have ssh keygen set up. Enter it now.

# Step 2: Jupyer Notebook on Remote Server (HPC)

You must now boot open a Jupyter Notebook session on the HPC by entering this command.

*Note: Do not copy and paste this straight into the command prompt. Copying this command directly from a web browser may encode some of the characters (like spaces) into something Linux does not understand. It is best to just manually enter this command.*

`jupyter notebook --no-browser --port=xxxx`

In selecting a port, you must select a number from 1024 to 49151. Don't close this terminal.

# Step 3: Connecting to Jupyter Notebook on your local machine

Finally, you will need to connect to the Jupyter Notebook server on your local machine. By creating a port on the HPC, you can created a path to connect to that server from any ssh terminal.

In another terminal on your local machine (not ssh'ed into HPC), enter this command:

`ssh -NfL localhost:xxxx:localhost:xxxx username@hpclogin.memphis.edu`

Make sure your port number is the same as the port you use in step 2. Again, do not copy and paste this into your terminal, but manually enter this command.

It should again ask for your login for HPC if you don't have ssh keygen set up. Enter it now.

# Step 4: Opening your Jupyter Notebook

On the HPC terminal you have open, it should have populated a link you can enter into your web browser and connect to.

Done!

# Troubleshooting

*Problem:* Sometimes, you will not be able to connect when you enter the link into your browser. Somewhere down the line, there is an issue connecting to the HPC. 

*Solution:* I try to restart my VPN conenction by turning off and on my wifi connection. This does not fully log me out of my VPN, but it will disconnect and attempt to reconnect when the wifi is connected again. Follow this by repeating Step 3 and sshing into your localhost server.

*Problem:* Port not working or "Address already in use"

*Solution:* You may be already connected to the port if you have tried this process eariler in the day. If so, entering the command from Step 3 is still necessary, but may not simply ask for your password. Otherwise, restart the process with another port number. 

*Problem:* "Error: forwarding specification"

*Solution:* Manually enter the commands, do not copy and paste them from somewhere else.

