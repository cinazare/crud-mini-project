import requests
from pprint import pprint
url="http://localhost:8000/tasks/"
payload = {
    "title": "Learn FastAPI 2",
    "description": "Work on CRUD functions",
    "is_completed": False
}

# print("----------------------------- POST ----------------------------------------")
# response = requests.post(
#     url=url, 
#     json=payload  
# )
# print("Status:", response.status_code)
# print("Response:", response.json())
# print("---------------------------------------------------------------------")

# print("----------------------------- GET ----------------------------------------")

# response = requests.get(
#     url=url, 
#     json=payload  
# )
# print("Status:", response.status_code)
# pprint(response.json())
# print("---------------------------------------------------------------------")


print("----------------------------- GET ----------------------------------------")
task_id = "1"
url=f"http://localhost:8000/tasks/{task_id}" 
response = requests.get(
    url=url, 
    json=payload
)
print("Status:", response.status_code)
pprint(response.json())
print("---------------------------------------------------------------------")

