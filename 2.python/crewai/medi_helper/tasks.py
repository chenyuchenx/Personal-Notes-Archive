from crewai import Task
from textwrap import dedent

class CustomTasks:

    def task_1(self, agent, name):
        return Task(
            description=dedent(
                f"""\
                    獲取 {name} 個人健康數據與飲食紀錄
                """
            ),
            expected_output = "個人健康數據與飲食紀錄",
            agent=agent,
        )
    
    def task_2(self, agent):
        return Task(
            description=dedent(
                f"""\
                    根據個人健康數據尋找病因
                """
            ),
            expected_output = "病因",
            agent=agent,
        )
    
    def task_3(self, agent):
        return Task(
            description=dedent(
                f"""\
                    根據病因尋找發病原因
                """
            ),
            expected_output = "血糖 病因 發病原因",
            agent=agent,
        )
    
    def task_4(self, agent):
        return Task(
            description=dedent(
                f"""\
                    根據發病原因尋找建議與處理方式
                """
            ),
            expected_output = "建議與處理方式",
            agent=agent,
        )
    
    def task_5(self, agent):
        return Task(
            description=dedent(
                f"""\
                    根據找建議與處理方式尋找最近的解決地點
                """
            ),
            expected_output = "最近的解決地點與距離",
            agent=agent,
        )
    
    def task_6(self, agent):
        return Task(
            description=dedent(
                f"""\
                    將所有思考的過程撰寫成一份全面的報告
                """
            ),
            expected_output = "撰寫一份全面的報告",
            agent=agent,
        )