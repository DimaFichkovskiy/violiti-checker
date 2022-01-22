from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMIN = env.str("ADMIN")

SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{env.str("DB_USER")}:{env.str("DB_PASSWORD")}@localhost:5432/admin'
SQLALCHEMY_TRACK_MODIFICATIONS = False
