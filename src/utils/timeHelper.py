import datetime


def get_now_date_str():
    dt = datetime.datetime.now()
    return str(dt.strftime("%Y-%m-%d %H:")) + "00:00"


# def get_china_date_str(utc_timestamp):
#     utc_time = pd.to_datetime(utc_timestamp, unit="ms")
#     time_delta = pd.Timedelta(8, unit="h")
#     result = utc_time + time_delta
#     return str(result.strftime("%Y-%m-%d %H:")) + "00:00"
#
#
# def convert_utc_milliseconds(str_):
#     """
#     Convert date to milliseconds
#     把日期转换成timestamp
#     : param str_: a str represents date, e.g. "2018-08-18"
#     : return: a int represents milliseconds
#     """
#     from_zone = tz.gettz('UTC')
#     ms = int(pd.Timestamp(str_).replace(tzinfo=from_zone).timestamp()*1000)
#     return ms
