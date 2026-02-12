from flask import Blueprint, render_template, request, jsonify
from app.services.ai_service import chatbot_reply

chatbot_bp = Blueprint("chatbot", __name__)

@chatbot_bp.route("/chat", methods=["GET"])
def chat_page():
    return render_template("chat.html")


@chatbot_bp.route("/api/chat", methods=["POST"])
def chat_api():
    data = request.get_json()
    user_message = data.get("message")

    response = chatbot_reply(user_message)

    return jsonify({"reply": response})
