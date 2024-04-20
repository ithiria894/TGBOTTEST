from typing import Final
from dotenv import load_dotenv
import os

load_dotenv()

# env variables
TOKEN: Final = os.getenv('TOKEN')
USERNAME: Final = os.getenv('USERNAME')
ACCESS_KEY: Final = os.getenv('ACCESS_KEY')
SECRET_KEY: Final = os.getenv('SECRET_KEY')
PASSPHRASE: Final = os.getenv('PASSPHRASE')

# endpoint
BASE_URL: Final = 'https://api.bitget.com'
AGENT_ENDPOINT: Final = '/api/broker/v1/agent/customerList'

# http header
CONTENT_TYPE: Final = 'Content-Type'
OK_ACCESS_KEY: Final = 'ACCESS-KEY'
OK_ACCESS_SIGN: Final = 'ACCESS-SIGN'
OK_ACCESS_TIMESTAMP: Final = 'ACCESS-TIMESTAMP'
OK_ACCESS_PASSPHRASE: Final = 'ACCESS-PASSPHRASE'
APPLICATION_JSON: Final = 'application/json'

# header key
LOCALE: Final = 'locale'

# method
GET: Final = "GET"
POST: Final = "POST"
DELETE: Final = "DELETE"

# sign type
RSA: Final = "RSA"
SHA256: Final = "SHA256"
SIGN_TYPE: Final = SHA256

# database
DATABASE_NAME: Final = 'uidList_database.csv'

# tg group id
EFFECTIVE_CHAT_ID: Final = '-1002087737560'
VIP_GROUP_ID: Final = '-1002043576596'
# CHAT_ID = '-1856345480'
# -1002043576596
# 4169810698