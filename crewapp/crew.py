from langsmith import Client
from crewai import Agent, Crew, Process, Task
from langchain_openai import ChatOpenAI
from textwrap import dedent
from pathlib import Path
from dotenv import load_dotenv
import importlib, yaml, json, os

load_dotenv()

print(os.getenv('LANGCHAIN_TRACING_V2'))
client = Client(api_key=os.getenv('LANGCHAIN_API_KEY'))

class CrewAIPipline:

    def __init__(self, data_or_file, retype, llm=None):
        self.data = self.load_file_data(data_or_file)
        self.type = retype
        self.llm = llm if llm is not None else ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)
        self.agent_methods = self.create_agents(self.data.get('agent', []))
        self.task_methods = self.create_tasks(self.data.get('tasks', []))
    
    def load_file_data(self, data_or_file):
        if isinstance(data_or_file, str):
            file_path = Path(data_or_file)
            if not file_path.exists():
                raise FileNotFoundError(f"File '{file_path}' not found")
            file_extension = file_path.suffix.lower()
            if file_extension == '.json':
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
            elif file_extension in ['.yml', '.yaml']:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = yaml.safe_load(file)
            else:
                raise ValueError("Unsupported file format")
        else:
            data = data_or_file
        return data
    
    def create_agents(self, agent_data):
        agent_methods = {}
        for agent_info in agent_data:
            agent_name = agent_info['name']
            role = agent_info['role']
            goal = agent_info['goal']
            backstory = dedent(agent_info.get('backstory', ''))
            allow_delegation = agent_info.get('allow_delegation', False)
            verbose = agent_info.get('verbose', True)
            tools = self.create_tools(agent_info.get('tools', []))
            agent_methods[agent_name] = self._create_agent_method(role, goal, backstory, allow_delegation, verbose, tools)
        return agent_methods
    
    def _create_agent_method(self, role, goal, backstory, allow_delegation, verbose, tools):
        def agent_method():
            return Agent(
                role=role,
                goal=goal,
                tools=tools,
                backstory=backstory,
                allow_delegation=allow_delegation,
                verbose=verbose,
                llm=self.llm
            )
        return agent_method
    
    def create_tasks(self, task_data):
        task_methods = {}
        for task_info in task_data:
            task_name = task_info['name']
            description = dedent(task_info['description'])
            description = description.replace('{type}', self.type) 
            expected_output = task_info['expected_output']
            agent = self.agent_methods[task_info['agent']]()
            task_methods[task_name] = self._create_task_method(description, expected_output, agent)
        return task_methods
    
    def _create_task_method(self, description, expected_output, agent):
        def task_method():
            return Task(
                description=description,
                expected_output=expected_output,
                agent=agent
            )
        return task_method
    
    def create_tools(self, tools_data):
        tools_func = []
        for tool in tools_data:
            module_name, func_name = tool.rsplit('.', 1)
            tools = importlib.import_module(f'tools')
            module = getattr(tools, module_name)
            func = getattr(module, func_name)
            print(module, func_name)
            tools_func.append(func)
        return tools_func
    
    def run(self, manager=False):

        agents = [agent() for agent in self.agent_methods.values()]
        tasks = [task() for task in self.task_methods.values()]

        crew_params = {
            'agents': agents,
            'tasks': tasks,
            'verbose': True,
            'process': Process.hierarchical if manager else Process.sequential
        }

        if manager:
            crew_params['manager_llm'] = self.llm

        crew = Crew(**crew_params)
        return crew.kickoff()
    
if __name__ == "__main__":
    
    #custom_crew = CrewAIPipline("./crewapp/gamemaker.json", "射擊遊戲")
    #custom_crew = CrewAIPipline("./crewapp/storymaker.yaml", "要先很生氣最後很的悲慘故事")
    custom_crew = CrewAIPipline("./crewapp/medihelper.yaml", "Lisa")
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)

