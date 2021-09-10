from website import dynamodb
from flask import Blueprint, request
from flask.templating import render_template

auth = Blueprint('auth', __name__)


@auth.route('/article', methods = ['GET'])
def article():
    return render_template('second.html')

@auth.route('/getArticle', methods = ['GET','POST'])
def getArticle():
    print("inside getArticle")
    if request.method == "POST":
        print("articleNumber is : " + request.data.decode("utf-8"))
        res = dynamodb.get_data(request.data.decode("utf-8").split("=")[1])
        print("returning " + res)
        return res
    else:
        return dynamodb.get_data("article1")


