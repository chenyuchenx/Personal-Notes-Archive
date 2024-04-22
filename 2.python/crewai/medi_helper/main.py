import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks

class CustomCrew:
    def __init__(self, name):
        self.name = name

    def run(self):
        agents = CustomAgents()
        tasks = CustomTasks()

        custom_agent_1 = agents.health_mgt_agent()
        custom_agent_2 = agents.medical_analytic_expert()

        custom_task_1 = tasks.task_1(custom_agent_1,self.name)
        custom_task_2 = tasks.task_2(custom_agent_1)
        custom_task_3 = tasks.task_3(custom_agent_1)
        custom_task_4 = tasks.task_4(custom_agent_2)
        custom_task_5 = tasks.task_5(custom_agent_2)
        custom_task_6 = tasks.task_6(custom_agent_2)

        crew = Crew(
            agents=[custom_agent_1, custom_agent_2],
            tasks=[custom_task_1, custom_task_2, custom_task_3, custom_task_4, custom_task_5, custom_task_6],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to MediHelper 的 AI 醫療助手")
    print("-------------------------------")
    name = input(dedent("""Enter your name: """))
    custom_crew = CustomCrew(name)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)