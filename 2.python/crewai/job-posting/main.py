from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

from tasks import Tasks
from agents import Agents

tasks = Tasks()
agents = Agents()

#company_description = input("What is the company description?\n")
#company_domain = input("What is the company domain?\n")
#hiring_needs = input("What are the hiring needs?\n")
#specific_benefits = input("What are specific_benefits you offer?\n")

company_description = """
Welcome to Essences, where innovation meets opportunity! We are a leading tech company dedicated to pushing the boundaries of artificial intelligence (AI) and revolutionizing industries worldwide.
At Essences, we're on a mission to harness the power of Python and AI to create cutting-edge solutions that transform the way businesses operate. Our team of talented engineers and data scientists work collaboratively to develop innovative AI algorithms, predictive models, and machine learning systems that drive success for our clients.
As a leader in the field of AI, we specialize in leveraging Python's robust libraries and frameworks, such as TensorFlow, PyTorch, and Scikit-learn, to build scalable and intelligent software solutions. From natural language processing (NLP) to computer vision and beyond, we're at the forefront of the AI revolution, shaping the future of technology one line of code at a time.
Join us at Essences] and become part of a dynamic team that's shaping the future of AI. With exciting projects, endless opportunities for growth, and a supportive work culture, there's no limit to what you can achieve with us.
Discover your potential with Essences today!
"""
company_domain = "https://www.essences.com.tw/"
hiring_needs = "We are currently seeking talented Python AI engineers to join our team and drive innovation in AI-powered solutions."
specific_benefits = "As part of our team, you'll enjoy competitive salaries, flexible work hours, ongoing training and development opportunities, and the chance to work on cutting-edge projects that make a real impact on the world."

# Create Agents
researcher_agent = agents.research_agent()
writer_agent = agents.writer_agent()
review_agent = agents.review_agent()

# Define Tasks for each agent
research_company_culture_task = tasks.research_company_culture_task(researcher_agent, company_description, company_domain)
industry_analysis_task = tasks.industry_analysis_task(researcher_agent, company_domain, company_description)
research_role_requirements_task = tasks.research_role_requirements_task(researcher_agent, hiring_needs)
draft_job_posting_task = tasks.draft_job_posting_task(writer_agent, company_description, hiring_needs, specific_benefits)
review_and_edit_job_posting_task = tasks.review_and_edit_job_posting_task(review_agent, hiring_needs)

# Instantiate the crew with a sequential process
crew = Crew(
    agents=[researcher_agent, writer_agent, review_agent],
    tasks=[
        research_company_culture_task,
        industry_analysis_task,
        research_role_requirements_task,
        draft_job_posting_task,
        review_and_edit_job_posting_task
    ]
)

# Kick off the process
result = crew.kickoff()

print("Job Posting Creation Process Completed.")
print("Final Job Posting:")
print(result)