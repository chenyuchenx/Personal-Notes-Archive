from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from tools.health_tools import HealthTools

class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def health_mgt_agent(self):
        return Agent(
            role="Personal Health Assistant",
            backstory="Experts in obtaining and analyzing medical and dietary records.",
            goal="Analyze personal health data to extract insights about dietary history and specific needs",
            tools=[
                HealthTools.scrape_diet_content,
                HealthTools.scrape_medical_knowledge_content,
                HealthTools.scrape_personal_health_content
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def medical_analytic_expert(self):
        return Agent(
            role="Medical Analytics Expert",
            backstory="Based on the search and suggested processing methods of the obtained medical records, search for the most recent solution location based on the suggested methods",
            goal="After analysis, we will provide suggestions for processing methods and the location of the processing methods",
            tools=[
                HealthTools.recommended_treatment,
                HealthTools.scrape_medical_knowledge_content,
                HealthTools.find_recent_purchases
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )