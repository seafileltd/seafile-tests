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


def get_metadata_enable_status():
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/"    
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}"
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"get_metadata_enable_status Status Code: {response.status_code}")

    row_data = {
        "Operation": "Get metadata enabled status",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)


def enable_metadata():
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}"
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.put(url, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"enable_metadata Status Code: {response.status_code}")

    row_data = {
        "Operation": "Enable metadata",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)


def disable_metadata():
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}"
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.delete(url, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"disable_metadata Status Code: {response.status_code}")

    row_data = {
        "Operation": "Disable metadata",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)


def details_settings(_columns: list[str] = []):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/details-settings/"
    payload = { "settings": { "columns": _columns } }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}"
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.put(url, json=payload, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"details_settings Status Code: {response.status_code}")

    row_data = {
        "Operation": "Detail settings",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)


def exract_file_details(_obj_ids: list[str]):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/extract-file-details/"
    payload = { "obj_ids": _obj_ids }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}"
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.post(url, json=payload, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"exract_file_details Status Code: {response.status_code}")

    row_data = {
        "Operation": "Extract file details",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)


if __name__ == "__main__":
    # details_settings(["_file_mtime"])
    # exract_file_details(["ad60423a854bc14ad7aa2d82c79bfbb9c7753478"])
    pass