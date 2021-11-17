from nuturelab import db


class Employees(db.Model):
    id = db.Column('employee_id', db.Integer, primary_key=True)
    user_id = db.Column(db.Integer())
    username = db.Column(db.String(100))
    Photo_url = db.Column(db.String(5000))
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __init__(self, user_id, username, photo_url):
        self.user_id = user_id
        self.username = username
        self.photo_url = photo_url
