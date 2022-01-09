import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    try:
        PORT = os.environ["PORT"]
        DB_URL = os.environ["DB_URL"]
        DB_USER = os.environ["DB_USER"]
        DB_PASSWORD = os.environ["DB_PASSWORD"]
        DB_DATABASE = os.environ["DB_DATABASE"]
        DB_HOST = os.environ["DB_HOST"]
        DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
            dbuser=DB_USER,
            dbpass=DB_PASSWORD,
            dbhost=DB_HOST,
            dbname=DB_DATABASE
        )
    except KeyError as e:
        raise Exception("Missing Environment Variable: %s" % str(e))
