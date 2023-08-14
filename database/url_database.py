from settings_env import pos_user, pos_pass, pos_host, pos_port, pos_db

_URL = f"postgresql://{pos_user}:{pos_pass}@{pos_host}:{pos_port}/{pos_db}"
