from telegraph import Telegraph
from langchain.llms import *
from langchain.agents import  *
import os

# Load API keys from environment variables
os.environ['SERPAPI_API_KEY'] = os.getenv('SERPAPI_API_KEY')
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
os.environ['WOLFRAM_ALPHA_APPID'] = os.getenv('WOLFRAM_ALPHA_APPID')

telegraph = Telegraph()
telegraph.create_account(short_name='1337')
llm = OpenAI(max_tokens=3000, temperature=0.7, top_p=1.0)

MAX_TITLE_WORDS = 8

def create_telegraph_page(title, text):
    """
    Create a page on Telegraph with a given title and text.
    """
    title = ' '.join(title.split()[:MAX_TITLE_WORDS])
    response = telegraph.create_page(
        title,
        html_content=text.replace('\n', '<br>').replace('h1', 'h3').replace('h2', 'h4')
    )
    link = f'<a href = "{response["url"]}">{title}</a>'
    return link

def generate_html(text):
    """
    Generate HTML from text.
    """
    return llm(f'(render in html only with tags h1,h2,h3,p,a): {text}')

def format_prompt(text):
    """
    Format a prompt for GPT-3.
    """
    return llm(f'Write a prompt for GPT-3 that will be easily understood by the AI and generate an accurate response: {text}')

def langchain_answer(prompt, tools):
    """
    Generate a Langchain answer.
    """
    tools = [
        Tool(
            name="Prompt-to-nice-prompt-formatting",
            func = format_prompt,
            description="Used always at start to write a prompt for GPT that will be easily understood by the AI and generate an accurate response.",
                ),
        *tools
    ]
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    answer = agent.run(prompt)
    answer = generate_html(answer)
    return create_telegraph_page(prompt, answer)
