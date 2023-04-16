from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    from .views import views

    app.register_blueprint(views)
    app.run(Debug=True, host="0.0.0.0")
