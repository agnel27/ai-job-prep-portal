import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def interview_feedback(question, answer):
    prompt = f"""
Score this answer out of 10.

Question: {question}
Answer: {answer}

Return:
Score: X
Feedback: text
"""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def resume_analysis(text):
    prompt = f"Analyze this resume:\n{text[:4000]}"
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def chatbot_reply(message):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a career advisor."},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content
