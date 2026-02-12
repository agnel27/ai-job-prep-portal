import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# ---------------------------
# Resume Analysis
# ---------------------------
def analyze_resume(resume_text):
    prompt = f"""
    You are a professional career coach.

    Analyze the following resume and provide:
    1. Strengths
    2. Weaknesses
    3. Suggestions for improvement
    4. Overall rating out of 10

    Resume:
    {resume_text}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful career assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


# ---------------------------
# Chatbot
# ---------------------------
def chatbot_reply(user_message):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a job preparation assistant."},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


# ---------------------------
# Interview Question Generator
# ---------------------------
def generate_interview_question(role):
    prompt = f"Generate one technical interview question for a {role}."

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are an interview coach."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


# ---------------------------
# Interview Feedback
# ---------------------------
def interview_feedback(question, answer):
    prompt = f"""
    You are an interview coach.

    Question:
    {question}

    Candidate Answer:
    {answer}

    Provide:
    1. Strengths
    2. Weaknesses
    3. Suggested improved answer
    4. Score out of 10
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are an interview evaluator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
