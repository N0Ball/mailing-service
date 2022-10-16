import os
from dotenv import load_dotenv

load_dotenv()

config = {
    'GOOGLE_MAIL': os.getenv("GOOGLE_MAIL"),
    'GOOGLE_SECRET': os.getenv("GOOGLE_SECRET"),
}

from .mail_conn import MAIL
mail = MAIL()