import requests

import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from constants import SEAFILE_SERVER_URL, REPO_ID, get_formatted_time, write_simple_result
from local_settings import SEAFILE_API_TOKEN

# def turn_on_ocr_feature():
#     url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/ocr/"
#     headers = {
#         "accept": "application/json",
#         "authorization": f"Bearer {SEAFILE_API_TOKEN}"
#     }
#     formatted_time = get_formatted_time()
#     try:
#         response = requests.put(url, headers=headers)
#     except Exception as e:
#         print(f"请求失败: {e}")
#     print(f"turn_on_ocr_feature Status Code: {response.status_code}")

#     row_data = {
#         "Operation": "Turn on OCR feature",
#         "Status Code": response.status_code,
#         "Response": response.text,
#         "Time": formatted_time
#     }
#     write_simple_result(row_data)

# def turn_off_ocr_feature():
#     url = f"{SEAFILE_SERVER_URL}/api/v2.1/repos/{REPO_ID}/metadata/ocr/"
#     headers = {
#         "accept": "application/json",
#         "authorization": f"Bearer {SEAFILE_API_TOKEN}"
#     }
#     formatted_time = get_formatted_time()
#     try:
#         response = requests.delete(url, headers=headers)
#     except Exception as e:
#         print(f"请求失败: {e}")
#     print(f"turn_off_ocr_feature Status Code: {response.status_code}")

#     row_data = {
#         "Operation": "Turn off OCR feature",
#         "Status Code": response.status_code,
#         "Response": response.text,
#         "Time": formatted_time
#     }
#     write_simple_result(row_data)

if __name__ == "__main__":
    #暂时请求失败
    pass