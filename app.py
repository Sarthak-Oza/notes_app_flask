from flask import Flask
from datab import db
from flask_login import LoginManager

print("before")

def app():
    print("after")
    
    app = Flask(__name__)

    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    db.init_app(app)
    
    from views import views
    
    from auth import auth

    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth, url_prefix = "/")
    
    from models import User, Note

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    with app.app_context():
        db.create_all()

    

    return app

if __name__ == "__main__":
    app = app()
    
    app.run(debug=True, port=5001)

