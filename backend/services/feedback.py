import os
from openai import OpenAI

prompt_one = '''
Here is a student ELA essay. Identify the greatest strength and biggest weakness in the writing sample.
Focus on higher-order concerns, such as:
- Strength and complexity of the argument
- Clarity and organization of ideas
- Factual accuracy
- Use of evidence and examples
Your response should be only two sentences, formatted like this:
Strength: [strength]
Weakness: [weakness]

'''

prompt_two = '''
You are a middle school ELA teacher providing feedback on a student essay.
You have identified a major strength and weakness in the writing sample.
Provide praise on the strength and constructive feedback on the weakness.
You should use language that is encouraging and supportive, suited for a middle school student,
and use helpful examples and/or comparisons to illustrate your points.
Your response should be 3-5 sentences, formatted like this:
Glow: [praise]
Grow: [constructive feedback]

Here is the student essay, followed by the strength and weakness you identified:

'''

client = OpenAI(
    base_url = "https://integrate.api.nvidia.com/v1",
    api_key = os.environ.get("NVIDIA_API_KEY")
)

def query_api(input: str):
    completion = client.chat.completions.create(
        model="nvidia/llama-3.1-nemotron-70b-instruct",
        messages=[{"role":"user","content":input}],
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

def generate_feedback(writing_sample: str):
    input_one = f"{prompt_one}\n{writing_sample}"

    response_one = query_api(input_one)
    print("RESPONSE ONE:\n\n")
    print(response_one)

    input_two = f"{prompt_two}\n{writing_sample}\n{response_one}"
    response_two = query_api(input_two)
    print("RESPONSE TWO:\n\n")
    print(response_two)


    return response_two



test = '''
The Hobbit is an adventurous novel about a hobbit named Frodo Baggins, who is asked by the wizard Gandalf to go on a dangerous journey. He joins a group of dwarves led by Thorin Oakenshield to reclaim their treasure from a dragon named Smaug. Along the way, they encounter many challenges like trolls, elves, and a creature called Gollum. Frodo finds a magical ring in Gollum’s cave that helps him escape, but he doesn’t know how powerful it is at first. This ring later becomes the main focus of another book called The Lord of the Rings.

One of the main themes of The Hobbit is courage. Frodo starts out as a timid hobbit who never leaves his home, but as the story progresses, he becomes braver and more confident. By the end of the journey, he is able to stand up to Smaug, showing that even the smallest person can make a big difference. This message is important because it teaches readers that anyone can be a hero, no matter how unlikely it seems.
'''