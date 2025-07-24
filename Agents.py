from crewai import Agent
from langchain_groq import ChatGroq

import os
from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

llm=ChatGroq(model='mistral-saba-24b')

#code writer agent
code_writer=Agent(
    role="Write the code.",
    goal="Generate functional and optimized code babsed on user prompts.",
    backstory="Expert in programming languages like python,java,C++,C,java script and other software based practices and frameworks.",
    verbose=True,
    llm=llm,
    allow_delegation=True,

)

#code debugger agent
code_debugger=Agent(
    role="Debug the code.",
    goal="Fix the any bugs and issues in the provided code and also explain your changes.",
    backstory="Senior engineer speacialized in debugging,refactoring and reasoning the code.",
    verbose=True,
    allow_delegation=False,
    llm=llm,

)

#complexity calculator
complexity_calculator=Agent(
    role="Analayze the complexity.",
    goal="Analyze the code complexity and explain in simple terms using Big-O notation.",
    llm=llm,
    backstory="Computer Science proffessor expertized in explaining algorithm's efficiency.",
    verbose=True,
    allow_delegation=False,
)