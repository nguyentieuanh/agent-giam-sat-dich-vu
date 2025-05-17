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

def load_alarm_device(id_device, data_loaded):
    content = ""
    for index, item in data_loaded.iterrows():
        content_item = ""
        pass


# file_path = "/Users/tieuanhnguyen/PycharmProjects/multiAgentChatbot/app_flow_service_vtnet/alarm_test/Core Mobile_Cảnh báo đơn lẻ_08052025.xlsx"
if __name__ == "__main__":
    file_path = "/Users/tieuanhnguyen/PycharmProjects/multiAgentChatbot/app_flow_service_vtnet/alarm_test/alarms_MSHT25.xlsx"
    data_loaded = load_data_file(file_path)
    content = ""
    columns = data_loaded.columns
    for index, item in data_loaded.iterrows():
        content_item = ""

    print("OK")