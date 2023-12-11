import requests
from credentials import token, username
from datetime import datetime

TOKEN = token
USERNAME = username
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# create new user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "page",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# create a pixelation graph
# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

# Post value to the graph. https://pixe.la/v1/users/niccr/graphs/graph1.html
pix_endpoint = f"{pixela_endpoint}/{username}/graphs/{GRAPH_ID}"

today = datetime.now()
formatted_date = today.strftime('%Y%m%d')

pixel_config = {
    "date": formatted_date,
    "quantity": "100"
}

# pixel_response = requests.post(url=pix_endpoint, json=pixel_config, headers=headers)
# print(pixel_response.text)

# update
pix_update_endpoint = f"{pix_endpoint}/{formatted_date}"
pixel_config_update = {
    "quantity": "200"
}
# pixel_update_response = requests.put(url=pix_update_endpoint, json=pixel_config_update, headers=headers)
# print(pixel_update_response.text)

# delete
# pixel_delete_response = requests.delete(url=pix_update_endpoint, headers=headers)
# print(pixel_delete_response.text)
