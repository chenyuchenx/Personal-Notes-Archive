from dotenv import load_dotenv
load_dotenv()

from crewai import Crew, Process
from textwrap import dedent
from tasks.game import GameTasks
from agents.game import GameAgents

class CustomCrew:
    def __init__(self, name):
        self.name = name

    def run(self):
        agents = GameAgents()
        tasks = GameTasks()

        custom_agent_1 = agents.senior_engineer_agent()
        custom_agent_2 = agents.qa_engineer_agent()
        custom_agent_3 = agents.chief_qa_engineer_agent()

        code_game = tasks.code_task(custom_agent_1, game)
        review_game = tasks.review_task(custom_agent_2, game)
        approve_game = tasks.evaluate_task(custom_agent_3, game)

        crew = Crew(
            agents=[custom_agent_1, custom_agent_2, custom_agent_3],
            tasks=[code_game, review_game, approve_game],
            verbose=True,
            process=Process.sequential
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to {Game} Crew")
    print("-------------------------------")
    game = input("What is the game you would like to build? What will be the mechanics?\n")
    custom_crew = CustomCrew(game)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)