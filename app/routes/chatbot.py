from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from app.services.ai_service import career_chat

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route("/chatbot")
@login_required
def chatbot():
    return render_template("chatbot.html")


@chatbot_bp.route("/chatbot/message", methods=["POST"])
@login_required
def chatbot_message():
    data = request.get_json()
    message = data.get("message", "")

    try:
        response = career_chat(message)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"response": "AI service error. Try again later."})
