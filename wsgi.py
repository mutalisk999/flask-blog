import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from flaskblog import create_app  # noqa

config_name = os.getenv('FLASK_CONFIG', 'development')
if config_name not in ('development', 'testing', 'production'):
    config_name = 'development'

app = create_app(config_name)
