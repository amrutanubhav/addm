# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:05:39 2020

@author: eamranu
"""

import requests
import pprint

hydra_entry=[]
network_id1=[]
agraj=[]

headers = {
        "Authorization": "63560792414a511fc61c79fbc121c2dff3106ba3",
        "verify": "hydra.cer"
          }


url_2 = "https://hydra.gic.ericsson.se/api/5.0/network"
data1 = {"token": "63560792414a511fc61c79fbc121c2dff3106ba3",
              
              "partition_id": '3802' ,
              "provider_id": '925' ,
              "consumer_id": '1950' ,
              "name": 'testnetworkathlone',
             # 'discovery_credential_id': '29' ,
             # 'discovery_organization_id': '29' ,
             # 'discovery_scanner_id': '5' ,
              'ipv4_address_domain_id': '1252',
              'ipv4_cidr': 24,
              'ipv4_end': None,
              'ipv4_start': '10.232.84.0'
              
              
              
              
              
}

response = requests.request("POST", url_2, data=data1, headers=headers)
json_text_1 = response.json()
container=json_text_1
network_id2= container['result']
netfetch = network_id2[0]
network_id1=netfetch['id']
hydra_entry.append(json_text_1)
pprint.pprint(hydra_entry)


headers_1 = {
        "Authorization": "63560792414a511fc61c79fbc121c2dff3106ba3",
        "verify": "hydra.cer"
          }

url_4 = "https://hydra.gic.ericsson.se/api/5.0/tag"
data4 = {"token": "63560792414a511fc61c79fbc121c2dff3106ba3",
        
         'l2_domain_id': '632' ,
         'network_id':network_id1 ,
         'tag' : '460' 
         
         
}

response = requests.request("POST", url_4, data=data4, headers=headers_1)
json_text_1 = response.json()
hydra_entry.append(json_text_1)
pprint.pprint(hydra_entry)
