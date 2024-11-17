import os
from dotenv import load_dotenv
import anthropic
from openai import OpenAI

# Load environment variables
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['ANTHROPIC_API_KEY'] = os.getenv('ANTHROPIC_API_KEY')
openai = OpenAI()
claude = anthropic.Anthropic()
OPENAI_MODEL = "gpt-4o"
CLAUDE_MODEL = "claude-3-5-sonnet-20240620"

system_message = """
    You are an assistant that reimplements Python code in high performance C++ for an M3 Mac. 
    Respond only with C++ code; use comments sparingly and do not provide any explanation other than occasional comments.
    The C++ response needs to produce an identical output in the fastest possible time.
    """

def user_prompt_for(python):
    user_prompt = """
        Rewrite this Python code in C++ with the fastest possible implementation that produces identical output in the least time. 
        Respond only with C++ code; do not explain your work other than a few comments. 
        Pay attention to number types to ensure no int overflows. Remember to #include all necessary C++ packages such as iomanip.\n\n
        """
    user_prompt += python
    return user_prompt

def messages_for(python):
    return [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_prompt_for(python)}
    ]

def stream_gpt(python):    
    stream = openai.chat.completions.create(model=OPENAI_MODEL, messages=messages_for(python), stream=True)
    reply = ""
    for chunk in stream:
        fragment = chunk.choices[0].delta.content or ""
        reply += fragment
        yield reply.replace('```cpp\n','').replace('```','')

def stream_claude(python):
    result = claude.messages.stream(
        model=CLAUDE_MODEL,
        max_tokens=2000,
        system=system_message,
        messages=[{"role": "user", "content": user_prompt_for(python)}],
    )
    reply = ""
    with result as stream:
        for text in stream.text_stream:
            reply += text
            yield reply.replace('```cpp\n','').replace('```','')

def optimize(python, model):
    if model=="GPT":
        result = stream_gpt(python)
    elif model=="Claude":
        result = stream_claude(python)
    else:
        raise ValueError("Unknown model")
    for stream_so_far in result:
        yield stream_so_far       