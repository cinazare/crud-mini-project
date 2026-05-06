import requests
from pprint import pprint
url="http://localhost:8000/tasks/"
payload = {
    "title": "Learn FastAPI 7",
    "is_completed": True
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
#     url=url
# )
# print("Status:", response.status_code)
# pprint(response.json())
# print("---------------------------------------------------------------------")


# print("----------------------------- GET ----------------------------------------")
# task_id = "8"
# url=f"http://localhost:8000/tasks/{task_id}" 
# response = requests.get(
#     url=url
# )
# print("Status:", response.status_code)
# pprint(response.text)
# print("---------------------------------------------------------------------")



# print("----------------------------- PATCH ----------------------------------------")
# task_id = "3"
# url=f"http://localhost:8000/tasks/{task_id}" 
# response = requests.patch(
#     url=url,
#     json=payload
# )
# print("Status:", response.status_code)
# pprint(response.json())
# print("---------------------------------------------------------------------")
