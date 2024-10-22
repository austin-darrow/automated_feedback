import torch
from transformers import AutoTokenizer
from llama_recipes.inference.model_utils import load_model

base_prompt = '''
The following is a student's writing sample. Please provide two (2) sentences of feedback.
The first sentence should praise a specific aspect of the writing sample.
The second sentence should provide constructive criticism.
The feedback should be encouraging and helpful.
Focus on content and ideas. Do not focus on grammar or spelling.
Student writing:

'''

# Load the Llama model and tokenizer
model_name = "meta-llama/Llama-3.2-3B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token  # Set pad_token to eos_token

# Load the model using llama-recipes utility
model = load_model(model_name=model_name, quantization=False)  # Quantization can be 4bit, 8bit for efficiency

def generate_feedback(writing_sample: str):
    # Concatenate the prompt and the student's writing sample into a single string
    input_text = f"{base_prompt}{writing_sample}"

    # Tokenize the input
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, padding=True)

    # Perform inference
    with torch.no_grad():
        outputs = model.generate(
            input_ids=inputs["input_ids"],
            max_new_tokens=200,  # You can adjust this based on your need
            do_sample=True,
            top_p=0.95,  # Top-p sampling for diverse results
            temperature=0.7,  # Controls randomness in generation
            repetition_penalty=1.2,  # Discourages repetition
            num_return_sequences=1,  # Number of feedbacks to generate
        )

    # Decode the output text
    feedback_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Remove input from output text
    feedback_text = feedback_text.replace(input_text, "")

    print(feedback_text)

    return feedback_text


test = '''
The Hobbit is an adventurous novel about a hobbit named Frodo Baggins, who is asked by the wizard Gandalf to go on a dangerous journey. He joins a group of dwarves led by Thorin Oakenshield to reclaim their treasure from a dragon named Smaug. Along the way, they encounter many challenges like trolls, elves, and a creature called Gollum. Frodo finds a magical ring in Gollum’s cave that helps him escape, but he doesn’t know how powerful it is at first. This ring later becomes the main focus of another book called The Lord of the Rings.

One of the main themes of The Hobbit is courage. Frodo starts out as a timid hobbit who never leaves his home, but as the story progresses, he becomes braver and more confident. By the end of the journey, he is able to stand up to Smaug, showing that even the smallest person can make a big difference. This message is important because it teaches readers that anyone can be a hero, no matter how unlikely it seems.
'''