from flask_sqlalchemy import SQLAlchemy
import json
 
db = SQLAlchemy()
 
class UserModel(db.Model):
    __tablename__ = "users"
 
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    attained_skills = db.Column(db.String())
    required_skills = db.Column(db.String())


 
    def __init__(self, name, attained_skills, required_skills):
        self.name = name
        self.attained_skills = attained_skills
        self.required_skills = required_skills
 
    def __repr__(self):
        return json.dumps({
            'user_id': self.user_id,
            'name': self.name,
            'attained_skills': json.loads(self.attained_skills),
            'required_skills': json.loads(self.required_skills)
        })



class ArticleModel(db.Model):
    __tablename__ = "articles"
 
    article_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    article_name = db.Column(db.String())


 
    def __init__(self, article_name, content):
        self.content = content
        self.article_name = article_name
 
    def __repr__(self):
        return json.dumps({
            'article_id': self.article_id,
            'article_name': self.article_name,
            'content': self.content
        })