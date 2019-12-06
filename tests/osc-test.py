from osc_sdk_python import Gateway
import json
if __name__ == '__main__':
    gw = Gateway(**{'profile': 'fne'})

    #for vm in gw.ReadVms()['Vms']:
     #   print(json.dumps(vm["SecurityGroups"]))
    vms = ((gw.ReadVms()['Vms']))
    VMs = dict()
    for vm in vms:
        VMs.update({vm['VmId'] : vm})
    #print  (VMs)
    #print(json.dumps(gw.ReadSecurityGroups()))

    #print("\nyour volumes:")
    #for volume in gw.ReadVolumes()["Volumes"]:
        #print(volume["VolumeId"])
    #ssgw1 = Gateway()
    #print(gw1.ReadSecurityGroups(  Filters = {    "SecurityGroupIds": [      "sg-c387f0b7"    ]})['SecurityGroups'][0]['InboundRules'])
    print(json.dumps(gw.ReadSecurityGroups(
                Filters={"SecurityGroupIds": ['sg-c387f0b7']}
            )["SecurityGroups"][0]["InboundRules"]))
    from requests import get