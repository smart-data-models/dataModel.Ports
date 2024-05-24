
#         # This code allows you to install a orion-ld broker in a linux system
#         # The manuals are here https://github.com/FIWARE/context.Orion-LD/tree/develop/doc/manuals-ld
#         
#         # INSTALL NGSI LD broker (OrionLD)
#         sudo docker pull mongo:3.6
#         sudo docker pull fiware/orion-ld
#         sudo docker network create fiware_default
#         sudo docker run -d --name=mongo-db --network=fiware_default --expose=27017 mongo:3.6 --bind_ip_all --smallfiles
#         sudo docker run -d --name fiware-orionld -h orion --network=fiware_default -p 1026:1026  fiware/orion-ld -dbhost mongo-db
#         
#         # TO RELAUNCH (only if you have already installed a broker in the same machine)
#         sudo docker stop fiware-orionld
#         sudo docker rm fiware-orionld
#         sudo docker stop mongo-db
#         sudo docker rm mongo-db
#         sudo docker network rm fiware_default
#         
#         # CHECK INSTANCES
#         # Check the broker is running
#         curl -X GET 'http://localhost:1026/version'
#         
#         # Check what entities are in the broker
#         curl -X GET http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000
#         
#         # now the python code you can use to insert some value in the context broker according to the data model
#         # Version Warning! 
#         # This code is designed to work with the version 0.8 of pysmartdatamodels or later
#         # to work with earlier version you need to replace the import instruction for
#         # from pysmartdatamodels import pysmartdatamodels as sdm
#         
#         
import pysmartdatamodels as sdm
import subprocess
serverUrl = "http://localhost:1026" # supposed that your broker is installed in localhost. Edit to match your configuration
dataModel = "SeaportFacilities"
subject = "dataModel.Ports"
dateLastReported = "2020-03-17T08:45:00Z"
attribute = "dateLastReported"
value = dateLastReported
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

refBoatAuthorized = ['urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-yatching', 'urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-passenger', 'urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-fishing', 'urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-cargo', 'urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-tankers', 'urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-specialist', 'urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-war', 'urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-historic']
attribute = "refBoatAuthorized"
value = refBoatAuthorized
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

refBoatPlaceAvailable = ['urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-A', 'urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-BC', 'urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-DE', 'urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-FG', 'urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-HI', 'urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-JK', 'urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-LO', 'urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-PQ', 'urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-RT2', 'urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-RT2', 'urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-U', 'urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-VW', 'urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-XZ', 'urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-Z02']
attribute = "refBoatPlaceAvailable"
value = refBoatPlaceAvailable
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

refBoatPlacePricing = ['urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-A', 'urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-BC', 'urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-DE', 'urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-FG', 'urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-HI', 'urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-JK', 'urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-LO', 'urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-PQ', 'urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-RT2', 'urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-RT2', 'urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-U', 'urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-VW', 'urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-XZ', 'urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-Z02']
attribute = "refBoatPlacePricing"
value = refBoatPlacePricing
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

print(" In case you have installed the orion-ld broker (see comments on the header of this program)")
print(" Execute this instruction to check that the entities has been inserted")
command = ['curl', '-X', 'GET', 'http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000']
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
