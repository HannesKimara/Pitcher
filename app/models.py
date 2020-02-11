from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from . import db

class User(UserMixin, db.Model):
    """
    User Class model to handle class instances in database

    """
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True)
    hash_pass = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref = 'user', lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.hash_pass = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.hash_pass, password)

    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):
    """
    Pitch Class model to handle pitch instances in database

    """
    __tablename__ = 'pitches'

    pitch_id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String(40))
    content = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    comments = db.relationship('Comment', backref = 'pitch', lazy = 'dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
        return self.pitch_id

    def get_category_pitches(self, pitch_category):
        return Pitch.query.filter_by(category=pitch_category).all()

    def get_user_pitches(self, user_id):
        return Pitch.query.filter_by(user_id = user_id).all()

    def __repr__(self):
        return f'Pitch {self.pitch_id}'

class Comment(db.Model):
    """
    Comment Class model to handle comment instances in database

    """
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String())
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.pitch_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        return self.comment_id

    def get_comments(self, pitch_id):
        return Comment.query.filter_by(pitch_id = pitch_id).all()
