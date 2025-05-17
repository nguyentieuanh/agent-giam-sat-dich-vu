from dconfig import config_object
from app_flow_service_vtnet.service import gemini_llm
from langchain.prompts import ChatPromptTemplate
from langchain.pydantic_v1 import BaseModel, Field
from app_flow_service_vtnet.common_utils.load_info import load_data_file_core_mobile, load_alarm_group_content,\
    load_group_id2match, load_data_file


class ResultNamedGroup(BaseModel):
    result: str = Field(description="Đây là các tên được đặt dựa trên đặc điểm chung của các cảnh báo hiện có. Giới hạn ngắn gọn súc tích.")
    reason: str = Field(description="Đây là lý do đặt tên đó")


#define chain
class NamedGroupAlarmChain:
    def __init__(self):
        prompt = ChatPromptTemplate.from_messages([
                ("system", config_object.RULE_NAMED_GROUP_ALARM),
                ("human", '{alarm_group_input}')
        ])
        structured_named_group_alarm = gemini_llm.with_structured_output(ResultNamedGroup)
        self.gen_result = prompt | structured_named_group_alarm


def reader(state):
    print(f'-----START READING----')
    reader_agent = NamedGroupAlarmChain()
    message = state["alarm_group"]
    result = reader_agent.gen_result.invoke({"alarm_group_input": message})
    state["ai_response"] = result
    print(f'-------END READING-------')
    return state


if __name__ == "__main__":
    from typing_extensions import TypedDict
    from typing import Optional

    class AgentState(TypedDict):
        alarm_group: Optional[str]
        ai_response: Optional[str]


    file_path = "alarm_test/Core Mobile_Cảnh báo đơn lẻ_08052025.xlsx"
    data_loaded = load_data_file_core_mobile(file_path)

    group_file = "alarm_test/15 nhom demo.xlsx"
    group_id = load_group_id2match(group_file)
    for id_group in group_id:
        content = load_alarm_group_content(data_loaded, id_group)

        state = AgentState(alarm_group=content, ai_response="")
        new_state = reader(state)
        print(f'Group id: {id_group}')
        print(new_state["ai_response"].result)
        print(new_state["ai_response"].reason)
