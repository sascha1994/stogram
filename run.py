from flask import Flask

from app.main.views import main_blueprint
from app.main.views import post_blueprint
from app.main.views import search_blueprint
from app.main.views import user_name_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_name_blueprint)


if __name__ == "__main__":
    app.run(debug=True)
