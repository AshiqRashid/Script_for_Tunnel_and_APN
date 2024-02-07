import json
import yaml
import subprocess
 
#Load JSON File
f = open('APNs.json')
json_data = json.load(f)


##############################################Build the tunnels

x = len(json_data)
for k in range(x):
    subprocess.call(['sh', './tunBuilder.sh', json_data[k]["dev"], json_data[k]["addr"]]) 
 
#############################################Operations on UPF.YAML  

#Load UPF.YAML File
with open('upf.yaml') as fh:
    upf_data = yaml.safe_load(fh)

#Compare

y = len(upf_data["upf"]["subnet"])

#OverRide
for i in range(y):
    upf_data["upf"]["subnet"][i]["addr"] = json_data[i]["addr"]
    upf_data["upf"]["subnet"][i]["dnn"] = json_data[i]["dnn"]
    upf_data["upf"]["subnet"][i]["dev"] = json_data[i]["dev"]

#Insert
for i in range(y,x):
    upf_data["upf"]["subnet"].insert(i, {"addr" : json_data[i]["addr"] , "dnn" : json_data[i]["dnn"], "dev" : json_data[i]["dev"]})

#Write on UPF.YAML
with open(r'upf.yaml', 'w') as file:
    documents = yaml.dump(upf_data, file)
 
#Copy to /etc/open5gs
subprocess.call(['sh', './copy.sh']) 


##############################################Operations on SMF.YAML
#Load YAML File
with open('smf.yaml') as fs:
    smf_data = yaml.safe_load(fs)

#Compare

z = len(smf_data["smf"]["subnet"])

#OverRide
for i in range(z):
    smf_data["smf"]["subnet"][i]["addr"] = json_data[i]["addr"]
    smf_data["smf"]["subnet"][i]["dnn"] = json_data[i]["dnn"]
    smf_data["smf"]["subnet"][i]["dev"] = json_data[i]["dev"]

#Insert
for i in range(z,x):
    smf_data["smf"]["subnet"].insert(i, {"addr" : json_data[i]["addr"] , "dnn" : json_data[i]["dnn"], "dev" : json_data[i]["dev"]})

with open(r'smf.yaml', 'w') as file:
    documents = yaml.dump(smf_data, file)

#Restart 
subprocess.call(['sh', './restart.sh'])
 
# Closing file
f.close()
