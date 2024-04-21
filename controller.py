from exceptions import BitgetAPIException
import bitget_api as baseApi
import constants
import utils
import datahelper
import datetime
import asyncio

async def is_valid_uid(message: str):
    if not message.isdigit():
        return False
    if datahelper.check_uid_list(constants.DATABASE_NAME, message):
        return False
    
    today = datetime.datetime.now()
    last_month = today.replace(day=1) - datetime.timedelta(days=1)
    epoch_ms = int(last_month.timestamp() * 1000)

    request = baseApi.BitgetApi(constants.ACCESS_KEY, constants.SECRET_KEY, constants.PASSPHRASE)
    try:
        params = {}
        params["uid"] = message
        params["startTime"] = str(epoch_ms)
        params["endTime"] = str(utils.get_timestamp())
        params["pageNo"] = 1
        params["pageSize"] = 1000
        response = await asyncio.to_thread(request.post, constants.AGENT_ENDPOINT, params)
    except BitgetAPIException as e:
        print("ERROR: " + e.message)
        return False

    current_uid_info: list = response['data']

    if not bool(current_uid_info):
        return False
        
    datahelper.add_uid_to_list(constants.DATABASE_NAME, message, True)
    return True
