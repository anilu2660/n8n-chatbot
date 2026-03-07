import requests


user_message = "summarise the recent 3 mails that i got using gmail tools"

request_message = {"message": user_message}

url = "https://anujup.app.n8n.cloud/webhook-test/684437fb-9068-4801-ad25-e2918697b22d"
response = requests.post(url, json=request_message)

print("Status:", response.status_code)
print("Raw response:", repr(response.text))

try:
    data = response.json()
    print("AI Response:", data[0]["output"])
except Exception as e:
    print("Could not parse response:", e)