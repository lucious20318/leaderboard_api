from app import db

class Leaderboard(db.Model):
    __tablename__ = 'Leaderboard'

    UID = db.Column(db.String(255), primary_key=True)
    Name = db.Column(db.String(255), nullable=False)
    Score = db.Column(db.Integer, nullable=False)
    Country = db.Column(db.String(255), nullable=False)
    TimeStamp = db.Column(db.TIMESTAMP, nullable=False)