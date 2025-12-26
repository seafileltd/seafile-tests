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


def turn_on_tags_feature():
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/tags-status/"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}"
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.put(url, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"turn_on_tags_feature Status Code: {response.status_code}")

    row_data = {
        "Operation": "Turn on tags feature",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

def turn_off_tags_feature():
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/tags-status/"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}"
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.delete(url, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"turn_off_tags_feature Status Code: {response.status_code}")

    row_data = {
        "Operation": "Turn off tags feature",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

def list_tags():
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/tags/"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}"
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"list_tags Status Code: {response.status_code}")

    row_data = {
        "Operation": "List tags",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)
    if response.status_code == 200:
        return response.text
    else:
        return None

def add_tags(_payload: dict):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/tags/"
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
    print(f"add_tags Status Code: {response.status_code}")

    row_data = {
        "Operation": "Add tags",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)
    if response.status_code == 200:
        return response.text
    else:
        return None

def update_tags(_payload: dict):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/tags/"
    payload = _payload
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
    print(f"update_tags Status Code: {response.status_code}")

    row_data = {
        "Operation": "Update tags",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

def delete_tags(_tag_ids: list[str]):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/tags/"
    payload = { 
        "tag_ids": _tag_ids
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
    print(f"delete_tags Status Code: {response.status_code}")

    row_data = {
        "Operation": "Delete tags",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

def update_file_tags(_payload: dict):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/file-tags/"
    payload = _payload
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
    print(f"update_file_tags Status Code: {response.status_code}")

    row_data = {
        "Operation": "Update file tags",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

def list_tag_files(_tag_id: str):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/tag-files/{_tag_id}/"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}"
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print(f"request failed: {e}")
    print(f"list_tag_files Status Code: {response.status_code}")

    row_data = {
        "Operation": "List tag files",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

def list_tags_files(_payload: dict):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/tags-files/"
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
    print(f"list_tags_files Status Code: {response.status_code}")

    row_data = {
        "Operation": "List tags files",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

def add_tags_links(_payload: dict):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/tags-links/"
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
    print(f"add_tags_links Status Code: {response.status_code}")

    row_data = {
        "Operation": "Add tags links",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

# def update_tags_links(_payload: dict):
#     url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/tags-links/"
#     payload = _payload
#     headers = {
#         "accept": "application/json",
#         "content-type": "application/json",
#         "authorization": f"Bearer {SEAFILE_API_TOKEN}",
#     }
#     formatted_time = get_formatted_time()
#     try:
#         response = requests.put(url, json=payload, headers=headers)
#     except Exception as e:
#         print(f"request failed: {e}")
#     print(f"update_tags_links Status Code: {response.status_code}")

#     row_data = {
#         "Operation": "Update tags links",
#         "Status Code": response.status_code,
#         "Response": response.text,
#         "Time": formatted_time
#     }
#     write_simple_result(row_data)

def delete_tags_links(_payload: dict):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/tags-links/"
    payload = _payload
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
    print(f"delete_tags_links Status Code: {response.status_code}")

    row_data = {
        "Operation": "Delete tags links",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

def merge_tags(_payload: dict):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/merge-tags/"
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
    print(f"merge_tags Status Code: {response.status_code}")

    row_data = {
        "Operation": "Merge tags",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

if __name__ == "__main__":
    # turn_on_tags_feature()
    # turn_off_tags_feature()
    # list_tags()
    # add_tags([
    #     {
    #         "_tag_name": "tagTest",
    #         "_tag_color": "#F4667C"
    #     }
    # ])
    # update_tags([
    #     {
    #         "tag_id": "AcqwwxjeQHeTeo1ExpPZbg",
    #         "tag": {
    #             "_tag_color": "#9860E5",
    #             "_tag_name": "newTagTest"
    #         }
    #     }
    # ])
    # delete_tags([
    #     "AcqwwxjeQHeTeo1ExpPZbg"
    # ])
    # update_file_tags({ 
    #     "file_tags_data": [
    #     {
    #         "tags": ["gXe6D6XhQmSmst5SizjAWQ",
    #                  "CzRlYMm1SiWrBiHHu5KH8Q"],
    #         "record_id": "-P52LX7KRPGO_lo273YEYg"
    #     }
    #     ]
    # })
    # list_tag_files("gXe6D6XhQmSmst5SizjAWQ")
    # list_tags_files({ 
    #     "tags_ids": ["gXe6D6XhQmSmst5SizjAWQ", "CzRlYMm1SiWrBiHHu5KH8Q"]
    # })
    # add_tags_links({
    #     "row_id_map": { "gXe6D6XhQmSmst5SizjAWQ": ["CzRlYMm1SiWrBiHHu5KH8Q"] },
    #     "link_column_key": "_tag_parent_links"
    # })
    # update_file_tags({
    #     "link_column_key": "_tag_parent_links",
    #     "row_id_map": { "gXe6D6XhQmSmst5SizjAWQ": ["CzRlYMm1SiWrBiHHu5KH8Q"] }
    # })
    # delete_tags_links({
    #     "link_column_key": "_tag_parent_links",
    #     "row_id_map": { "gXe6D6XhQmSmst5SizjAWQ": ["CzRlYMm1SiWrBiHHu5KH8Q"] }
    # })
    # merge_tags({
    #     "merged_tags_ids": ["gXe6D6XhQmSmst5SizjAWQ"],
    #     "target_tag_id": "CzRlYMm1SiWrBiHHu5KH8Q"
    # })
    pass