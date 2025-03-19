from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPENAI_KEY'))



users_goal = ''

def set_user_goal(text : str):
    users_goal = text
    if users_goal:
        return True
    return False



def create_motivational_quote():
    global users_goal
    """
        Create a message for the user to help them get motivated and stay consistent. 
    """
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", 
            "content": f"You are a helpful assistant that is going to motivate this user in reaching their goals using good psychology tricks and give the user more than just generic motivation, something that will actually have an impact and help them reach their goal"
            }, 
            {"role":"user", "content": f"My goal is: {users_goal}"}
            
        ]
    )
    return completion.choices[0].message