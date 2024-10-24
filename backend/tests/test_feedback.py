from fastapi.testclient import TestClient
from backend.main import app as fastapi_app

client = TestClient(fastapi_app)

test_essay = '''
The Hobbit is an adventurous novel about a hobbit named Frodo Baggins, who is asked by the wizard Gandalf to go on a dangerous journey. He joins a group of dwarves led by Thorin Oakenshield to reclaim their treasure from a dragon named Smaug. Along the way, they encounter many challenges like trolls, elves, and a creature called Gollum. Frodo finds a magical ring in Gollum’s cave that helps him escape, but he doesn’t know how powerful it is at first. This ring later becomes the main focus of another book called The Lord of the Rings.

One of the main themes of The Hobbit is courage. Frodo starts out as a timid hobbit who never leaves his home, but as the story progresses, he becomes braver and more confident. By the end of the journey, he is able to stand up to Smaug, showing that even the smallest person can make a big difference. This message is important because it teaches readers that anyone can be a hero, no matter how unlikely it seems.
'''

def test_generate_feedback():
    params = {
        "writing_sample": test_essay
    }
    response = client.post("/api/feedback/1/1", params=params)
    response_text = response.json()['feedback']
    assert 'Glow' in response_text
    assert 'Grow' in response_text