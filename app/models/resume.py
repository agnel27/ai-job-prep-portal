from app import db
from datetime import datetime

class ResumeAnalysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    result = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
