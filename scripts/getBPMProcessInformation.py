import urllib3, requests, json
bpmusername='admin'
bpmpassword='admin'
bpmrestapiurl = 'https://localhost:9443/rest/bpm/wle/v1'

headers = urllib3.util.make_headers(basic_auth='{username}:{password}'.format(username=bpmusername, password=bpmpassword, verify=False))

url = bpmrestapiurl + '/processApps'
response = requests.get(url, headers=headers, verify=False)

[processApp] = [x for x in json.loads(response.text).get('data').get('processAppsList') if x.get('name') == 'Recommendation Service']
processAppId = processApp.get('ID')
print("the process application id: " + processAppId)
snapshot = processApp.get('installedSnapshots')[0]
versionId = snapshot.get('ID')
print("the process application version id: " + versionId)


url = bpmrestapiurl + '/assets'
response = requests.get(url, headers=headers, verify=False, params={'processAppId': processAppId, 'filter': 'type=BPD' })

[processId] = [x.get('poId') for x in json.loads(response.text).get('data').get('BPD') if x.get('name') == 'Claim Approval']

print('The process id : ' + processId);

print('The process version id : ' + versionId);


response = requests.get(url, headers=headers, verify=False, params={'processAppId': processAppId, 'filter': 'type=TrackingGroup' })

[trackingGroupId] = [x.get('poId') for x in json.loads(response.text).get('data').get('TrackingGroup') if x.get('name') == 'IBMBPMRSTraining_Claims']

print('The tracking group id : ' + trackingGroupId);

print('The tracking group version : ' + versionId);
