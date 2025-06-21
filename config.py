from dotenv import load_dotenv
import os
# Load environment variables from .env file
from app import app

load_dotenv()
app.config['SECRET_KEY'] = os.getenv ('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False').lower() in ['true', '1', 'yes']