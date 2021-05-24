from pyproject import db




class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    username = username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    diabetes = db.relationship('Diabetes', backref='name', lazy=True)

def __repr__(self):
        return f"User('{self.username}', '{self.email}')"