from flask import Flask, request, jsonify, Response
from utils import translate, summarize
import json
from models import db, UserModel, ArticleModel

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skillathon.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()

@app.route('/content/translate', methods=['POST'])
def translate_api():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        body = request.json

        text = body['text']
        to = body['to']

        translated = translate(text, to)
        result = {
            'text': text,
            'translated': translated
        }
        json_string = json.dumps(result,ensure_ascii = False)
        response = Response(json_string,content_type="application/json; charset=utf-8" )
        return response

        
    else:
        return 'Content-Type not supported!'


@app.route('/content/summarize', methods=['POST'])
def summarize_api():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        body = request.json

        text = body['text']
        lines = body['lines']

        translated = summarize(text, lines)
        result = {
            'text': text,
            'summary': translated
        }
        json_string = json.dumps(result,ensure_ascii = False)
        response = Response(json_string,content_type="application/json; charset=utf-8" )
        return response

        
    else:
        return 'Content-Type not supported!'




@app.route('/content/summarize-and-translate', methods=['POST'])
def summarize_and_translate_api():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        body = request.json

        text = body['text']
        to = body['to']
        lines = body['lines']

        summarized = summarize(text, lines)
        translated = translate(summarized, to)
        result = {
            'text': text,
            'translated_summary': translated
        }
        json_string = json.dumps(result,ensure_ascii = False)
        response = Response(json_string,content_type="application/json; charset=utf-8" )
        return response

        
    else:
        return 'Content-Type not supported!'


@app.route('/users' , methods = ['POST'])
def create_user():

    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        body = request.json

        name = body['name']
        try:
            attained_skills = json.dumps(body['attained_skills'])
            required_skills = json.dumps(body['required_skills'])
        except:
            return Response('Invalid array format found. attained_skills and required_skills should be valid array.', status=400)

        user = UserModel(name, attained_skills, required_skills)
        db.session.add(user)
        db.session.commit()
        print(user)
        response = Response(str(user),content_type="application/json; charset=utf-8" )
        return response

        
    else:
        return 'Content-Type not supported!'


@app.route('/users')
def RetrieveUserDataList():
    users = UserModel.query.all()
    response = Response(str(users),content_type="application/json; charset=utf-8" )
    return response


@app.route('/users/<int:id>')
def RetrieveSingleUser(id):
    user = UserModel.query.filter_by(user_id=id).first()
    if user:
        response = Response(str(user),content_type="application/json; charset=utf-8" )
        return response
    return Response('User with given id not found.', status=404)


@app.route('/users/<int:id>',methods = ['PATCH'])
def updateUser(id):
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        body = request.json

        name = body['name']
        try:
            attained_skills = json.dumps(body['attained_skills'])
            required_skills = json.dumps(body['required_skills'])
        except:
            return Response('Invalid array format found. attained_skills and required_skills should be valid array.', status=400)

        user = UserModel.query.filter_by(user_id=id).update(dict(name=name, attained_skills=attained_skills, required_skills=required_skills))
        user = UserModel.query.filter_by(user_id=id).first()
        db.session.commit()
        response = Response(str(user),content_type="application/json; charset=utf-8" )
        return response

        
    else:
        return 'Content-Type not supported!'


@app.route('/users/<int:id>', methods=['DELETE'])
def deleteUser(id):
    user = UserModel.query.filter_by(user_id=id).first()
    if request.method == 'DELETE':
        if user:
            db.session.delete(user)
            db.session.commit()
        else:
            return Response('User with given id not found.', status=404)

 
    response = Response(str(user),content_type="application/json; charset=utf-8" )
    return response



@app.route('/articles' , methods = ['POST'])
def createArticle():

    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        body = request.json

        article_name = body['article_name']
        content = body['content']

        article = ArticleModel(article_name, content)
        db.session.add(article)
        db.session.commit()
        print(article)
        response = Response(str(article),content_type="application/json; charset=utf-8" )
        return response

        
    else:
        return 'Content-Type not supported!'


@app.route('/articles')
def RetrieveArticleDataList():
    articles = ArticleModel.query.all()
    response = Response(str(articles),content_type="application/json; charset=utf-8" )
    return response


@app.route('/articles/<int:id>')
def RetrieveSingleArticle(id):
    article = ArticleModel.query.filter_by(article_id=id).first()
    if article:
        response = Response(str(article),content_type="application/json; charset=utf-8" )
        return response
    return Response('Article with given id not found.', status=404)


@app.route('/articles/<int:id>',methods = ['PATCH'])
def updateArticle(id):
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        body = request.json

        article_name = body['article_name']
        content = body['content']

        article = ArticleModel.query.filter_by(article_id=id).update(dict(article_name=article_name, content=content))
        article = ArticleModel.query.filter_by(article_id=id).first()
        db.session.commit()
        response = Response(str(article),content_type="application/json; charset=utf-8" )
        return response

        
    else:
        return 'Content-Type not supported!'


@app.route('/articles/<int:id>', methods=['DELETE'])
def deleteArticle(id):
    article = ArticleModel.query.filter_by(article_id=id).first()
    if request.method == 'DELETE':
        if article:
            db.session.delete(article)
            db.session.commit()
        else:
            return Response('Article with given id not found.', status=404)

 
    response = Response(str(article),content_type="application/json; charset=utf-8" )
    return response



if __name__ == '__main__':
    app.run(debug=True)