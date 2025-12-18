from seatable_api import Base, context
import time
from local_settings import SEATABLE_API_TOKEN


# --- Seafile 配置 ---
SEAFIEL_SERVER_URL = "https://dev.seafile.com/seahub"
REPO_ID = "dc06e4ec-95f3-4005-88d0-dd18029f5ea6"

# --- SeaTable 配置 ---
SEATABLE_SERVER_URL = context.server_url or 'https://dev.seatable.cn'
TABLE_NAME = "Table1" 

# --- 获取当前时间并格式化 ---
def get_formatted_time():
    timestamp = time.time()
    return time.strftime("%Y-%m-%d %H:%M", time.localtime(timestamp))

# --- SeaTable 写入逻辑 ---
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
    #写入测试结果
    base.append_row(TABLE_NAME,row_data)

    # 批量删除前3行测试数据
    # rows = base.list_rows(TABLE_NAME)
    # del_rows = rows[:3]
    # row_ids = [row['_id'] for row in del_rows]
    # base.batch_delete_rows('Table1', row_ids)

