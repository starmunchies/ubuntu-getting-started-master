
import requests
import json 

ip = "https://management.azure.com/subscriptions/1ecb891d-5996-461a-8aa6-57815d8b9ddb/resourceGroups/bobby/providers/Microsoft.Compute/virtualMachines/killmeB?api-version=2022-08-01"
headers= {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSIsImtpZCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0Lzc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYS8iLCJpYXQiOjE2NjgwOTE1NjgsIm5iZiI6MTY2ODA5MTU2OCwiZXhwIjoxNjY4MDk3MDc4LCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFRBQUFBS1htSkQrOE9mTklvWFVEUmFoMjRGNm9IQlAwSitHK05BaVF4TDU1bHd2S2xlL1VCMHVxTUZtY2F1K1BiMHoxOEFmbmQwYU1SRDNVSWJLS1k2TTIxRVphVG56SmY0b1RmQ1VNS2t5dDhCelU9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiUnVzc2VsbCIsImdpdmVuX25hbWUiOiJNYXR0aGV3IiwiZ3JvdXBzIjpbImQyYTZhOGVmLTRkMjYtNGQ5NS1iZDExLWFhMWVjNjE5ZjgxOCIsIjk3YWY4MTJkLTk2ZTktNGYwMS04YTExLTc1ODAzMzc2MjE3YSIsIjhjODE4NmVhLTQyYTQtNDRhZi04YTc4LWFlOTE0MDExZTZiNCIsIjVhZDdkNmI0LWFkYWYtNGI5ZC05NTdmLTBmM2I2MTRiZWU2MCIsIjEyNWNhYjdjLWY5ZWItNDNlNS05ZTIxLTVlM2I1ZGRkMDViYSIsIjhhYzE1NGRkLWQ0NWYtNGM0Ni05NGU1LWJiNzhmZWZhM2FlZiJdLCJpcGFkZHIiOiI4MC4yMzMuNDMuMTUzIiwibmFtZSI6IkMyMDMzNjA0NiBNYXR0aGV3IFJ1c3NlbGwiLCJvaWQiOiI3NjUwYjZmMC1hNTNmLTRhZjktYWQ3My1iMzU2ZTU0ZGMyZWUiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMjAyNTQyOTI2NS0xOTU4MzY3NDc2LTcyNTM0NTU0My0zMjYzOTkiLCJwdWlkIjoiMTAwMzIwMDBFNEFFMzhBNCIsInJoIjoiMC5BVEVBeXhkamRranBYMDZNN05xOGppX1Yya1pJZjNrQXV0ZFB1a1Bhd2ZqMk1CTXhBQ3cuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiaEpBTEFtVnRMY0llMWx5RjNYajViMGk1UHhXTTFhMWphQU1iWUNDaTdmRSIsInRpZCI6Ijc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYSIsInVuaXF1ZV9uYW1lIjoiQzIwMzM2MDQ2QG15dHVkdWJsaW4uaWUiLCJ1cG4iOiJDMjAzMzYwNDZAbXl0dWR1Ymxpbi5pZSIsInV0aSI6IjU1Q2o5VlZjbUVpOFp3VGZnZEdpQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfdGNkdCI6MTUyNTMzODk0MX0.n33EZ8YKJLg6Op_OJYIlya63dTWRM1oqnFYwxi9e67ce7s4nOZTok0LlCFVLc_YtlIBvE2lYFUThYVgsVQKTiJuwNDe8ZHQAb1kMY9KC2TnmyUDt-2X_zrqblp5ZLkyXDjpvjtySeprdZ3pHiPmzrxZ5yOO4al_iDFHXfogPPDq1dUA_2uaSQAQtAF9pwT-tzGe3xnQtFV94QnS-3ZP3b7ERWrBQic6YlLjIvry5qdFFT7ItBy5mxzgtQc6bUqVZ2Cd-xxIjvpmVn4pFg4MzPE4qA43xcI3XAzAg6A9FfvtKz7nmVHA2d0R5ZSphL4wbQy7EO4MRP9iadcFDnPd17g",
"Content-type": "application/json"}

body = {
"id": "/subscriptions/1ecb891d-5996-461a-8aa6-57815d8b9ddb/resourceGroups/bobby/providers/Microsoft.Compute/virtualMachines/myVM",
"type": "Microsoft.Compute/virtualMachines",
"properties": {
"osProfile": {
"adminUsername": "paul",
"secrets": [
],
"computerName": "myVM",
"linuxConfiguration": {
"ssh": {
"publicKeys": [
{
"path": "/home/paul/.ssh/authorized_keys",
"keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDA6/K0HCRzf6dHmuT0hcaipQy9ds8R9ZNHaQx6MUSitftAprx2h5oWeD90bPzI6wFTxE556xyQvrOHlRBHoR+Gmxq7rmxfuFuoxCg3SMNc2lu4Kwelu5sgwxeOPzF5BV2mut/968GPpxcMOTnEuC7wjKsT0EG1dS1to2hckwCH3LX9v005xyVtm569WnIC4wmcUmK4PwWfYM+koB82WpD4sDOtzBky01PjrkeFK1G+6uYcVF5mbTqjs8y4ZSNvSKi6kZ3oWr46aCU0HJpD3/54o1byY2V2S8ZsO+Jfidl6acO0tGyA0sYy8ieW+WufBwzHtjNGOBCkKt7Jdx3yic20YHkMcgAa9vJqwz/AhAA9C6T8TI1wwIqXECvaU0samhQiFuLM1XMD9QCzSv9SHWMadiE9Ehusjek5qdk6unUxdhXfbjDxed9Ayo6I4VeEPMnnIqrVyoeyevrO7zzTzIJAP3Vpm0E3hdKKLA2TtJIYrPSkkviUh91wid2hcw36Adk= matthew@Starmunchies"
}
]
},
"disablePasswordAuthentication": True
}
},
"networkProfile": {
"networkInterfaces": [
{
"id": "/subscriptions/1ecb891d-5996-461a-8aa6-57815d8b9ddb/resourceGroups/bobby/providers/Microsoft.Network/networkInterfaces/networkintB",
"properties": {
"primary": True
}
}
]
},
"storageProfile": {
"imageReference": {
"sku": "16.04-LTS",
"publisher": "Canonical",
"version": "latest",
"offer": "UbuntuServer"
},
"dataDisks": [
]
},
"hardwareProfile": {
"vmSize": "Standard_D1_v2"
},
"provisioningState": "Creating"
},
"name": "killmeB",
"location": "uksouth"
}

query = requests.put(ip,data=json.dumps(body),headers=headers)
print(query.status_code)
print(query.text)


