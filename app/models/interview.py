from app import db

class InterviewResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Float, default=0)
    feedback = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())