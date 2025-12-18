import requests
from typing import TypedDict, List, Dict

import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from constants import SEAFILE_SERVER_URL, REPO_ID, get_formatted_time, write_simple_result
from local_settings import SEAFILE_API_TOKEN


def list_metadata_records(_view_id: str, _start: int, _limit: int):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/records/?view_id={_view_id}&start={_start}&limit={_limit}"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}"
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print(f"请求失败: {e}")
    print(f"list_metadata_records Status Code: {response.status_code}")

    row_data = {
        "Operation": "List metadata records",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)


class RecordItem(TypedDict):
    record_id: str
    _obj_id: str
    record: Dict[str, str]

class PayloadStructure(TypedDict):
    records_data: List[RecordItem]

def update_metadata_records(_payload: PayloadStructure):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/records/"
    
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
        print(f"请求失败: {e}")
    print(f"update_metadata_records Status Code: {response.status_code}")

    row_data = {
        "Operation": "Update metadata records",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

def get_metadata_record(_parent_dir: str, _file_name: str):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/record/?parent_dir={_parent_dir}&file_name={_file_name}"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {SEAFILE_API_TOKEN}"
    }
    formatted_time = get_formatted_time()
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print(f"请求失败: {e}")
    print(f"get_metadata_record Status Code: {response.status_code}")

    row_data = {
        "Operation": "Get metadata record",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

def update_metadata_record(_parent_dir: str, _file_name: str, _data: dict):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/record/"
    
    payload = {
        "parent_dir": _parent_dir,
        "file_name": _file_name,
        "data": _data
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
        print(f"请求失败: {e}")
    print(f"update_metadata_record Status Code: {response.status_code}")

    row_data = {
        "Operation": "Update metadata record",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

# _column_data 接收json对象
def add_column(_column_name: str, _column_key: str, _column_type: str, _column_data: dict = None):
    url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/columns/"
    payload = {
        "column_name": _column_name,
        "column_key": _column_key,
        "column_type": _column_type,
        "column_data": _column_data
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
        print(f"请求失败: {e}")
    print(f"add_column Status Code: {response.status_code}")

    row_data = {
        "Operation": "Add column",
        "Status Code": response.status_code,
        "Response": response.text,
        "Time": formatted_time
    }
    write_simple_result(row_data)

if __name__ == "__main__":
    # list_metadata_records("zfl0", 0, 10)
    # update_metadata_record("/", "test.sdoc", {"_description": "18888"})
    
    # add_column("testColumn", "testColumn", "text")
    # get_metadata_record("/", "test.sdoc")

    # data: PayloadStructure = {
    #     "records_data": [
    #         {
    #             "record_id": "n9vyqgI4SRugwJ-yLxKTWw",
    #             "_obj_id": "f876cec256027ded8710441e49f33eac61515c59",
    #             "record": {
    #                 "_description": "00000",
    #             }
    #         }
    #     ]
    # }
    # update_metadata_records(data)
    pass