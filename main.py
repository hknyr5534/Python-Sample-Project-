import json

from RestApiTool import RestApiTool
import requests

request = RestApiTool()
request.requester_id = 4
request.requester_name = "administrator"
request.impact_details = "Detaylar"
request.subject = "Test Python"
request.description = "Test Açıklaması"

print(request.createRequest())

url = "https://servicedeskplus.manageengine.com.tr/api/v3/requests"
headers = {"authtoken": "981AFA7C-0513-4D4B-88BB-9484FF3377BB"}

data = {'input_data': request.createRequest()}
response = requests.post(url, headers=headers, data=data, verify=False)

y = json.loads(response.text)
if y["response_status"]["status_code"] == 2000:
    print("Başarılı")
else:
    print("Sunucu hatası")
