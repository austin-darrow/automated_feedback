import os
from openai import OpenAI

client = OpenAI(
    base_url = "https://integrate.api.nvidia.com/v1",
    api_key = os.environ.get("NVIDIA_API_KEY")
)

def query_api(messages: list):
    completion = client.chat.completions.create(
        model="nvidia/llama-3.1-nemotron-70b-instruct",
        messages=messages,
        temperature=0.5,
        top_p=1,
        max_tokens=1024,
        stream=True
    )

    response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content

    return response

def generate_feedback(writing_sample: str, focus: str = None):
    if not focus:
        focus = '''higher-order concerns, such as:
- Strength and complexity of the argument
- Clarity and organization of ideas
- Factual accuracy
- Use of evidence and examples'''

    system_prompt = f'''
You are a middle school ELA teacher providing feedback on a student essay.

First, identify the greatest strength and biggest weakness in the writing sample.
Focus on {focus}

Your identification should be only two sentences, formatted like this:
Strength: [strength]
Weakness: [weakness]

Then, provide praise on the strength and constructive feedback on the weakness.
Use language that is encouraging and supportive, suited for a middle school student,
and use helpful examples, relevant comparisons, or thought-provoking questions to illustrate your points.
Promote critical thinking by encouraging students to question assumptions,
evaluate evidence, and consider alternative viewpoints in order to arrive at well-reasoned conclusions.

Your final response should be 3-5 sentences, formatted like this:
Glow: [praise]
Grow: [constructive feedback]

'''

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": writing_sample}
    ]

    response = query_api(messages)
    print("RESPONSE:\n\n")
    print(response)

    return response