from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from app.services.ai_service import generate_interview_feedback
from app.models.interview import InterviewResult
from app import db
import re

interview_bp = Blueprint("interview", __name__)

@interview_bp.route("/interview", methods=["GET", "POST"])
@login_required
def interview():
    question = "Explain OOP."

    if request.method == "POST":
        answer = request.form["answer"]
        result = generate_interview_feedback(question, answer)

        match = re.search(r"Score:\s*(\d+)", result)
        score = int(match.group(1)) if match else 0

        record = InterviewResult(
            user_id=current_user.id,
            score=score,
            feedback=result
        )
        db.session.add(record)
        db.session.commit()

        return render_template("interview.html", result=result, question=question)

    return render_template("interview.html", question=question)
