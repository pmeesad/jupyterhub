# jupyterhub/create_admin.py
import requests
import json
import time
import os

JUPYTERHUB_URL = "http://jupyterhub.localhost:8081/hub/api"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "^1965ABx*"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"token {os.getenv('JUPYTERHUB_API_TOKEN')}"
}

# Define user payload
user_payload = {
    "username": ADMIN_USERNAME,
    "password": ADMIN_PASSWORD
}

# Wait for JupyterHub to be ready
time.sleep(10)

# Create the admin user
response = requests.post(f"{JUPYTERHUB_URL}/users", headers=headers, data=json.dumps(user_payload))

if response.status_code == 201:
    print(f"User {ADMIN_USERNAME} created successfully.")
else:
    print(f"Failed to create user: {response.content}")

# Promote user to admin
response = requests.post(f"{JUPYTERHUB_URL}/authorizations/role/admin/users/{ADMIN_USERNAME}", headers=headers)

if response.status_code == 201:
    print(f"User {ADMIN_USERNAME} promoted to admin successfully.")
else:
    print(f"Failed to promote user to admin: {response.content}")
