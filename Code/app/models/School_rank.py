from app import db


class Rank2017(db.Model):
    __tablename__ = 'rank2017'
    # roll_number = db.Column(db.String(50), db.ForeignKey('school.roll_number'), primary_key=True)
    place_id = db.Column(db.String(50), db.ForeignKey('school.place_id'), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    rank = db.Column(db.Integer)
    p_rank = db.Column(db.Integer)
    gender_type = db.Column(db.String(50))
    at_university = db.Column(db.Float(10))  # ?
    at_third_level = db.Column(db.Float(10))
    boy = db.Column(db.Integer)
    girl = db.Column(db.Integer)
    stu_tea_ratio = db.Column(db.Float(10))  # ?
