import os
# DEFINE CONSTANTS

# POSTGRES DB SETTINGS
DB_HOST = os.getenv('DB_HOST', False)
DB_PORT = os.getenv('DB_PORT', False)
DB_USER = os.getenv('DB_USER', False)
DB_PASS = os.getenv('DB_PASS', False)
DB_NAME = os.getenv('DB_NAME', False)



if not all([DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME]):
    print(f'[WARN] database settings incomplete!')


CONNECTION_STRING = f'dbname={DB_NAME} user={DB_USER} password={DB_PASS}, host={DB_HOST} port={DB_PORT}'

