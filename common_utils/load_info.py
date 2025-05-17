import pandas as pd


def load_data_file_core_mobile(file_path):
    data_loaded = pd.read_excel(file_path,
                                sheet_name="Sheet1")
    return data_loaded


def load_data_file(file_path):
    data_loaded = pd.read_excel(file_path)
    return data_loaded


def load_alarm_group_content(data_loaded, group_id):
    data_group = data_loaded[data_loaded["alarm_group_id"]==group_id]
    # data_group = data_group[data_group["device_code"]==id_device]
    content = ""
    list_alarm = []
    for index, item in data_group.iterrows():
        line = f'Alarm {item["alarm_id"]}: Nội dung cảnh báo là {item["content"]}\n'
        list_alarm.append(line)
        content += line
    return content


#TODO: Hàm load thông tin thiết bị
def load_alarm_device(id_device, data_loaded):
    content = ""
    for index, item in data_loaded.iterrows():
        content_item = ""
        pass


# Hàm lấy thông tin các nhóm cần đặt tên
def load_group_id2match(file_path):
    data_loaded = pd.read_excel(file_path)
    group_id = data_loaded["alarm_group_id"].unique()
    return list(group_id)
