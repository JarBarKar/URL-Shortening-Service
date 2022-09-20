import os

# mySQL Account Detail

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{os.environ.get("DB_ACCOUNT_ID")}:{os.environ.get("DB_ACCOUNT_PASSWORD")}@127.0.0.1:3306/tiny-url-clone'

SQLALCHEMY_TRACK_MODIFICATIONS = False