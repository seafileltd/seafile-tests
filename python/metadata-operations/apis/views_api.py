import requests

import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
granfparent_dir = os.path.dirname(parent_dir)
sys.path.append(granfparent_dir)
sys.path.append(parent_dir)
from constants import SEAFILE_SERVER_URL, REPO_ID, get_formatted_time, write_simple_result
from local_settings import SEAFILE_API_TOKEN


def list_views():
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/views/"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}"
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"list_views Status Code: {response.status_code}")

    row_data = {
        "Operation": "List views",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)
    if response.status_code == 200:
        return response.text
    else:
        return None

def add_view(_payload: dict):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/views/"
    payload = _payload
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}",
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.post(url, json=payload, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"add_view Status Code: {response.status_code}")

    row_data = {
        "Operation": "Add view",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)
    if response.status_code == 200:
        return response.text
    else:
        return None

def update_view(_view_id: str, _view_name: str):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/views/"
    payload = {
        "view_id": _view_id,
        "view_data": {"name": _view_name}
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}",
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.put(url, json=payload, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"update_view Status Code: {response.status_code}")

    row_data = {
        "Operation": "Update view",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

def delete_view(_view_id: str):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/views/"
    payload = {
        "view_id": _view_id
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}",
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.delete(url, json=payload, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"delete_view Status Code: {response.status_code}")

    row_data = {
        "Operation": "Delete view",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

def get_a_view(_view_id: str):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/views/{_view_id}"
    # payload = { 
    #     "view_id": _view_id 
    # }
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}",
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"get_a_view Status Code: {response.status_code}")

    row_data = {
        "Operation": "Get a view",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

def move_view(_source_view_id: str, _target_view_id: str):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/move-views/"
    payload = {
        "source_view_id": _source_view_id,
        "target_view_id": _target_view_id
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}",
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.post(url, json=payload, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"move_view Status Code: {response.status_code}")

    row_data = {
        "Operation": "Move view",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

def duplicate_view(_view_id: str):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/duplicate-view/"
    payload = {
        "view_id": _view_id
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}",
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.post(url, json=payload, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"duplicate_view Status Code: {response.status_code}")

    row_data = {
        "Operation": "Duplicate view",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)


if __name__ == "__main__":
    # list_views()
    # add_view("New Test View")
    # update_view("4jmf", "NewViewName")
    # delete_view("4jmf")
    # get_a_view("f72b")
    # move_view("zb6q", "f72b")
    # duplicate_view("f72b")
    pass