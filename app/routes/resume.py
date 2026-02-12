from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
import os
from werkzeug.utils import secure_filename

from app import db
from app.models.resume import ResumeAnalysis
from app.services.file_service import extract_text_from_file
from app.services.ai_service import analyze_resume

resume_bp = Blueprint('resume', __name__)

ALLOWED_EXTENSIONS = {"pdf", "docx"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@resume_bp.route("/resume", methods=["GET", "POST"])
@login_required
def resume():
    result = None

    if request.method == "POST":
        file = request.files.get("resume")

        if not file or file.filename == "":
            flash("Please upload a file", "danger")
            return redirect(request.url)

        if not allowed_file(file.filename):
            flash("Only PDF and DOCX files are allowed", "danger")
            return redirect(request.url)

        filename = secure_filename(file.filename)
        upload_folder = current_app.config["UPLOAD_FOLDER"]
        os.makedirs(upload_folder, exist_ok=True)

        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)

        try:
            text = extract_text_from_file(filepath)
            ai_result = analyze_resume(text)

            # Save to database
            record = ResumeAnalysis(
                user_id=current_user.id,
                suggestions=ai_result.get("suggestions"),
                keywords=ai_result.get("keywords"),
                ats_score=ai_result.get("ats_score"),
            )
            db.session.add(record)
            db.session.commit()

            result = ai_result

        except Exception as e:
            flash("Error analyzing resume. Try again.", "danger")
            print("Resume error:", e)

    return render_template("resume.html", result=result)
