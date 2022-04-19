from flask import Flask
import config
from blueprints import user_bp, content_bp

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(user_bp)
app.register_blueprint(content_bp)

if __name__ == '__main__':
    app.run()