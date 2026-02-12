from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.interview import InterviewResult
from app.models.resume import ResumeAnalysis

analytics_bp = Blueprint('analytics', __name__)


@analytics_bp.route("/analytics")
@login_required
def analytics():
    interviews = InterviewResult.query.filter_by(user_id=current_user.id).all()
    resumes = ResumeAnalysis.query.filter_by(user_id=current_user.id).all()

    total_interviews = len(interviews)
    avg_score = (
        sum(i.score for i in interviews) / total_interviews
        if total_interviews > 0
        else 0
    )

    total_resumes = len(resumes)

    return render_template(
        "analytics.html",
        total_interviews=total_interviews,
        avg_score=round(avg_score, 1),
        total_resumes=total_resumes,
    )
