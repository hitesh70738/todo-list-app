from application import db


class Tasks(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    task_name = db.Column(db.String(50), nullable=False)
    task_completion = db.Column(db.Boolean(), nullable=False, default=False) 
    task_description = db.Column(db.String(100), nullable=False)
