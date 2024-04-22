from crewai import Agent
from crewai_tools.tools import WebsiteSearchTool, SerperDevTool, FileReadTool
from langchain_openai import AzureChatOpenAI, ChatOpenAI
import os

web_search_tool = WebsiteSearchTool()
seper_dev_tool = SerperDevTool()
file_read_tool = FileReadTool(
	file_path='job_description_example.md',
	description='A tool to read the job description example file.'
)

azure_llm = AzureChatOpenAI(
    azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
    api_key=os.environ.get("AZURE_OPENAI_KEY"),
    temperature=0.2,
)

class Agents():

	def __init__(self):
		self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
		self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

	def research_agent(self):
		return Agent(
			role='Research Analyst',
			goal='Analyze the company website and provided description to extract insights on culture, values, and specific needs.',
			tools=[web_search_tool, seper_dev_tool],
			backstory='Expert in analyzing company cultures and identifying key values and needs from various sources, including websites and brief descriptions.',
			verbose=True,
			llm=self.OpenAIGPT35
		)

	def writer_agent(self):
			return Agent(
				role='Job Description Writer',
				goal='Use insights from the Research Analyst to create a detailed, engaging, and enticing job posting.',
				tools=[web_search_tool, seper_dev_tool, file_read_tool],
				backstory='Skilled in crafting compelling job descriptions that resonate with the company\'s values and attract the right candidates.',
				verbose=True,
			    llm=self.OpenAIGPT35
			)

	def review_agent(self):
			return Agent(
				role='Review and Editing Specialist',
				goal='Review the job posting for clarity, engagement, grammatical accuracy, and alignment with company values and refine it to ensure perfection.',
				tools=[web_search_tool, seper_dev_tool, file_read_tool],
				backstory='A meticulous editor with an eye for detail, ensuring every piece of content is clear, engaging, and grammatically perfect.',
				verbose=True,
			    llm=self.OpenAIGPT35
			)