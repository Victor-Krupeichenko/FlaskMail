import os
from dotenv import load_dotenv

load_dotenv()

pos_host = os.getenv("POSTGRES_HOST")
pos_port = os.getenv("POSTGRES_PORT")
pos_user = os.getenv("POSTGRES_USER")
pos_pass = os.getenv("POSTGRES_PASSWORD")
pos_db = os.getenv("POSTGRES_DB")

redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")
redis_db = os.getenv("REDIS_DB")

secrets_key_csrf = os.getenv("SECRET_KEY_CSRF")

save_path_file = os.getenv("SAVE_PATH_FILE")

smtp_user = os.getenv("SMTP_USER")
smtp_password = os.getenv("SMTP_PASSWORD")
smtp_host = os.getenv("SMTP_HOST")
smtp_port = os.getenv("SMTP_PORT")
mail_text = os.getenv("TEXT")
mail_subject = os.getenv("SUBJECT")
