from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain.agents import load_tools
from langchain_openai import AzureChatOpenAI
import os

llm = AzureChatOpenAI(
    openai_api_version=os.environ.get("AZURE_OPENAI_VERSION", "2024-02-15-preview"),
    azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT", "gpt-35-turbo-0613"),
    azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT", "https://ifactory-openai.openai.azure.com"),
    api_key=os.environ.get("AZURE_OPENAI_KEY")
)

@CrewBase
class WeeklyReportCrew():
    """WeeklyReport crew"""
    agents_config = 'agents/weekly.yaml'
    tasks_config = 'tasks/weekly.yaml'
 
    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'],
            verbose=True,
            llm=llm, 
            allow_delegation=True
        )
 
    @agent
    def sender(self) -> Agent:
        return Agent(
            config=self.agents_config['sender'],
            verbose=True,
            llm=llm, 
            allow_delegation=True
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'],
            agent=self.writer()
        )
 
    @task
    def send_task(self) -> Task:
        return Task(
            config=self.tasks_config['send_task'],
            agent=self.sender(),
            context=[self.writing_task()]
    )

    @crew
    def crew(self) -> Crew:
        """Creates the WeeklyReport crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
            process=Process.sequential,
            manager_llm=llm,
        )

if __name__ == "__main__":
    print("## Welcome to {Game} Crew")
    print("-------------------------------")
    #game = input("What is the game you would like to build? What will be the mechanics?\n")
    custom_crew = WeeklyReportCrew()
    result = WeeklyReportCrew().crew().kickoff()
    print("##################")
    print(result)
    print("##################")