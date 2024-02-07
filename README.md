# Script_for_Tunnel_and_APN

This script is able to create multiple tunnels and APNs.

# INSTRUCTION    
Follow the below steps to create multiple tunnels and APNs using the script 
**1.** Copy Tunnel_Automation.py, tunBuilder.sh, copy.sh, restart.sh, and APNs.json files to /etc/open5gs/ location.

**2.** Inside APNs.json, write the information of your APN and Tunnel which you want to create in json format. Add your tunnel’s information inside the curly bracket. Here, dnn is the APN name and dev is the Tunnel name.
***Caution:*** Remember during writing inside this APNs.json file, you should not edit the first APN’s information.

    {
        "addr": "10.45.0.1/24",
        "dnn": "internet",
        "dev": "ogstun"
    },
    {
        "addr": "10.46.0.1/24",
        "dnn": "robi",
        "dev": "robi_tunnel"
    },
    {
        "addr": "10.47.0.1/24",
        "dnn": "gp",
        "dev": "gp_tunnel"
    },
    {
        "addr": "10.48.0.1/24",
        "dnn": "nybsys",
        "dev": "nyb_tunnel"
    }

In the above APNs.json, we see, three additional APNs are written along with the default one (i.e. the first APN)

**3.** Now run the Tunnel_Automation.py from /etc/open5gs/ directory.

    cd /etc/open5gs
    sudo python3 Tunnel_Automation.py

Running this script, all the specified tunnels and APNs will be created.

# CHECK
We can check whether the tunnels have been created or not in many ways. 

FIRST: 

We can check the IP address of the machine to see whether the tunnels have been created or not.

Before running the program,

Before running the program,
2.png

After running the program,
3.png

SECOND:

![image](https://github.com/AshiqRashid/Script_for_Tunnel_and_APN/assets/136219283/fb65dc94-c34e-4761-8099-58b7789d60dc)


2.png

After running the program,

3.png

SECOND:

The upf.yaml will also be updated after running the program.

Before running the program,
4.png

After running the program,
Screenshot from 2023-08-24 10-54-49.png

 

THIRD:

The smf.yaml will also be updated after running the program.

Before running the program,
6.png

After running the program,
Screenshot from 2023-08-24 10-55-48.png
Note:
The APNs and tunnels created using this program are not persistent after rebooting. Though they are erased, but, the smf.yaml and upf.yaml files hold information of the erased APNs and tunnels. So, after rebooting, you need to edit smf.yaml and upf.yaml files and remove information of the erased APNs and tunnels manually.   
