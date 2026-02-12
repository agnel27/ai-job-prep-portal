import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_interview_feedback(answer, question):
    prompt = f"""
    You are an interview coach.

    Question: {question}
    Candidate Answer: {answer}

    Give:
    1. Score out of 10
    2. Short feedback
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content


def analyze_resume(resume_text):
    prompt = f"""
    Analyze this resume and give:
    - Strengths
    - Weaknesses
    - Suggestions

    Resume:
    {resume_text}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content


def career_chat(message):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful career assistant.",
            },
            {"role": "user", "content": message},
        ],
        temperature=0.5,
    )

    return response.choices[0].message.content
