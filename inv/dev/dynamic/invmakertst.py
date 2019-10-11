#!/usr/bin/python3

import json

iplist = []
iplistuname = {}
iptotallist = {}
meta = {}
g = {}
k = {}
m = {}

with open("/home/student/ans/inv/dev/dynamic/listoips.txt", "r") as listips:
    for line in listips:
        if "backbone_bbr" in line:
            for line in listips:
                 if line[0] == '#' or line[0] == "\n":
                     break

                 # Remove end of line '\'" from line
                 line = line.strip('\n')
                 
                 # Split Line into separate items for list
                 line = line.split()

                 # Item gets added to iplist
                 
                 iplist.append(line[0])

                 # Username gets added to iplistuname
                 
                 k['ansible_ssh_user'] = line[1]
                 #print(k)
                 m = line[0]
                 iplistuname[m] = k
                 k = {}
                 m = {}
                 #print(iplistuname)

x = iplist 
iptotallist['hosts'] = x
z = iplistuname
meta['hostvars'] = z 

g = {}
g['all'] = iptotallist
g['_meta'] = meta
print(json.dumps(g))

#print(meta)

#print(iptotallist & meta)
#print(g)
#"group": {
#        "hosts": [
#            "192.168.28.71",
#            "192.168.28.72"
#        ],
#        "vars": {
#            "ansible_ssh_user": "johndoe",
#            "ansible_ssh_private_key_file": "~/.ssh/mykey",
#            "example_variable": "value"
#        }
#    },
#    "_meta": {
#        "hostvars": {
#            "192.168.28.71": {
#                "host_specific_var": "bar"
#            },
#            "192.168.28.72": {
#                "host_specific_var": "foo"
#            }
#        }
#    }
#}
