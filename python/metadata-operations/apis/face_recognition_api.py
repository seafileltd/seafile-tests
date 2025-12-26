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


def get_face_recognition_enabled_status():
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/face-recognition/"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}"
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"get_face_recognition_enabled_status Status Code: {response.status_code}")

    row_data = {
        "Operation": "Get face recognition enabled status",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

def open_face_recognition():
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/face-recognition/"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}"
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.post(url, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"open_face_recognition Status Code: {response.status_code}")

    row_data = {
        "Operation": "Open face recognition",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

def list_face_records(_start: int =0, _limit: int =1000):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/face-records/?start={_start}&limit={_limit}"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}"
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"list_face_records Status Code: {response.status_code}")

    row_data = {
        "Operation": "List face records",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)
    if response.status_code == 200:
        return response.text
    else:
        return None

def list_people_photos(_people_id: str, _start: int =0, _limit: int =1000):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/people-photos/{_people_id}/?start={_start}&limit={_limit}"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}"
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"list_people_photos Status Code: {response.status_code}")

    row_data = {
        "Operation": "List people photos",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)
    if response.status_code == 200:
        return response.text
    else:
        return None

def remove_people_photos(_people_id: str, _payload: dict = None):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/people-photos/{_people_id}/"
    payload = _payload
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}"
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.delete(url, json=payload, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"remove_people_photos Status Code: {response.status_code}")

    row_data = {
        "Operation": "Remove people photos",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

# def add_people_photos(_people_id: str, _payload: dict = None):
#     url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/people-photos/{_people_id}/"
#     payload = _payload
#     headers = {
#         "accept": "application/json",
#         "content-type": "application/json",
#         "authorization": f"Bearer {SEAFILE_API_TOKEN}"
#     }
#     formatted_time = get_formatted_time()
#     try:
#         response = requests.post(url, json=payload, headers=headers)
#     except Exception as e:
#         print(f"request failed: {e}")
#     print(f"add_people_photos Status Code: {response.status_code}")

#     row_data = {
#         "Operation": "Add people photos",
#         "Status Code": response.status_code,
#         "Response": response.text,
#         "Time": formatted_time
#     }
#     write_simple_result(row_data)

# def update_face_name(_payload: dict = None):
#     url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/face-record/"
#     payload = _payload
#     headers = {
#         "accept": "application/json",
#         "content-type": "application/json",
#         "authorization": f"Bearer {SEAFILE_API_TOKEN}"
#     }
#     formatted_time = get_formatted_time()
#     try:
#         response = requests.put(url, json=payload, headers=headers)
#     except Exception as e:
#         print(f"request failed: {e}")
#     print(f"update_face_name Status Code: {response.status_code}")

#     row_data = {
#         "Operation": "Update face name",
#         "Status Code": response.status_code,
#         "Response": response.text,
#         "Time": formatted_time
#     }
#     write_simple_result(row_data)

def update_people_cover_photo(_people_id: str, _payload: dict = None):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/people-cover-photo/{_people_id}/"
    payload = _payload
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
    print(f"update_people_cover_photo Status Code: {response.status_code}")

    row_data = {
        "Operation": "Update people cover photo",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

if __name__ == "__main__":
    # get_face_recognition_enabled_status()
    # open_face_recognition()
    # list_face_records(0, 10)
    # list_people_photos("LZQ_sH2lTguOCKR76Gmm4w", 0, 5)
    # remove_people_photos("LZQ_sH2lTguOCKR76Gmm4w", { "record_ids": ["wQAzg1GAQV6-FWmKmUNqgw"] })
    # # add_people_photos("LZQ_sH2lTguOCKR76Gmm4w", { "record_ids": ["7dmU4bf2RhW_tii3qMLZYA"] })
    # # update_face_name({
    # #     "record_id": "1gquLClnRl-o3roFtT6fEg",
    # #     "name": "newName"
    # # })
    # update_people_cover_photo("LZQ_sH2lTguOCKR76Gmm4w", { "record_id": "l52n-YEsReqIovE8F1_bHw" })
    pass