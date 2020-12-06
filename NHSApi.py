import requests
response = requests.get("https://sandbox.api.service.nhs.uk/hello-world/hello/world")
print(response.json())
