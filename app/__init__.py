import os 

from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SENGRID_KEY=os.environ.get('SENGRID_API_KEY'),
        SECRET_KEY='mikey'
    )

    from . import portfolio

    app.register_blueprint(portfolio.bp)

    return app