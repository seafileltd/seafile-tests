from seatable_api import Base, context
import time

import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from local_settings import SEATABLE_API_TOKEN


# --- Seafile Config ---
SEAFILE_SERVER_URL = "https://dev.seafile.com/seahub"
REPO_ID = "dc06e4ec-95f3-4005-88d0-dd18029f5ea6"

# --- SeaTable Config ---
SEATABLE_SERVER_URL = context.server_url or 'https://dev.seatable.cn'
TABLE_NAME = "Table1" 

def get_formatted_time():
    timestamp = time.time()
    return time.strftime("%Y-%m-%d %H:%M", time.localtime(timestamp))

def write_simple_result(row_data):
    base = Base(SEATABLE_API_TOKEN, SEATABLE_SERVER_URL)
    base.auth()

    #test
    '''
    row_data = {
        "Operation": "Test Write",
        "Status Code": 000,
        "Response": "text",
        "Time": "1997-01-01 00:00"
    }
    '''
    base.append_row(TABLE_NAME,row_data)