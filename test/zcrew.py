from crewai import Agent, Crew, Process, Task
from langchain_openai import ChatOpenAI
from textwrap import dedent
import yaml, json

class CrewAITasks:
    def __init__(self, agent_methods):
        self.agent_methods = agent_methods

    def create_tasks(self, task_data):
        task_methods = {}
        for task_info in task_data:
            task_name = task_info['name']
            description = dedent(task_info['description'])
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

class CrewAIAgents:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

    def create_agents(self, agent_data):
        agent_methods = {}
        for agent_info in agent_data:
            agent_name = agent_info['name']
            role = agent_info['role']
            goal = agent_info['goal']
            backstory = dedent(agent_info.get('backstory', ''))
            allow_delegation = agent_info.get('allow_delegation', False)
            verbose = agent_info.get('verbose', True)
            agent_methods[agent_name] = self._create_agent_method(role, goal, backstory, allow_delegation, verbose)
        return agent_methods

    def _create_agent_method(self, role, goal, backstory, allow_delegation, verbose):
        def agent_method():
            return Agent(
                role=role,
                goal=goal,
                backstory=backstory,
                allow_delegation=allow_delegation,
                verbose=verbose,
                llm=self.llm
            )
        return agent_method

class CustomCrew:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def run(self):
        agents = CrewAIAgents()
        agent_methods = agents.create_agents(self.data['agent'])

        tasks = CrewAITasks(agent_methods)
        task_methods = tasks.create_tasks(self.data['tasks'])

        custom_agent_1 = agent_methods['qa_engineer_agent']()
        custom_agent_2 = agent_methods['senior_engineer_agent']()

        code_game = task_methods['code_task']()
        review_game = task_methods['review_task']()

        crew = Crew(
            agents=[custom_agent_1, custom_agent_2],
            tasks=[code_game, review_game],
            verbose=True,
            #process=Process.hierarchical,
            #manager_llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
            process=Process.sequential
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to {Game} Crew")
    print("-------------------------------")
    game = input("What is the game you would like to build? What will be the mechanics?\n")
    
    with open('data.yaml', 'r') as file:
        data = yaml.safe_load(file)
    json_data = json.dumps(data, indent=2)
    print(json_data)

    custom_crew = CustomCrew(game, data)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
