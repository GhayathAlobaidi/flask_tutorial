from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello.  This is Dewystone Testing Portal.  Please press here.'
