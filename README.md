# Script_for_Tunnel_and_APN

In LTE and 5G, we ofter need multiple APNs and tunnels for various reasons including service differentiation, security, roaming and network management. Here we have developed scripts which can automate tunnel and APN creation. We just need to specify all the required APNs and tunnels in a json file and this script is able to create all that tunnels and APNs.

# INSTRUCTION    
Follow the below steps to create multiple tunnels and APNs using the script

**1.** Locate Tunnel_Automation.py, tunBuilder.sh, copy.sh, restart.sh, and APNs.json files to the location where all the yaml files of the services of Open5gs (particularly, upf.yaml and smf.yaml) are located. In most cases, this location is  /etc/open5gs/ and we have specified this location in copy.sh script. If you have a different location for yaml files, edit copy.sh file accordingly.

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

***FIRST:*** 

We can check the IP address of the machine to see whether the tunnels have been created or not.

Before running the program,

![image](https://github.com/AshiqRashid/Script_for_Tunnel_and_APN/assets/136219283/7160331e-68ef-46df-a1eb-35a0080fbb73)

After running the program,

![image](https://github.com/AshiqRashid/Script_for_Tunnel_and_APN/assets/136219283/466ffea2-f755-4284-8765-11be1311a70e)


***SECOND:***
The upf.yaml will also be updated after running the program.

Before running the program,

![image](https://github.com/AshiqRashid/Script_for_Tunnel_and_APN/assets/136219283/2ee984bb-7d9d-4220-9e86-215caeffebe2)

After running the program,

![image](https://github.com/AshiqRashid/Script_for_Tunnel_and_APN/assets/136219283/593a734f-a42f-4df8-8a94-dff37b013c92)

***THIRD:***

The smf.yaml will also be updated after running the program.

Before running the program,

![image](https://github.com/AshiqRashid/Script_for_Tunnel_and_APN/assets/136219283/6dcb3790-b7bb-4fca-b32b-9b0f9026c6c7)

After running the program,

![image](https://github.com/AshiqRashid/Script_for_Tunnel_and_APN/assets/136219283/957ee455-34aa-4044-854e-598028618b5b)


**Note:**
The APNs and tunnels created using this program are not persistent after rebooting. Though they are erased, but, the smf.yaml and upf.yaml files hold information of the erased APNs and tunnels. So, after rebooting, you need to edit smf.yaml and upf.yaml files and remove information of the erased APNs and tunnels manually.   
