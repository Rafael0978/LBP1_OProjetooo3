from flask import Flask
from controllers.teste import hello_controller

app = Flask(__name__)

app.register_blueprint(hello_controller)


if __name__=="__main__":
	app.run(debug=True) 
