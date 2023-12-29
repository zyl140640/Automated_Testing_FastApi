from datetime import datetime


# 生成当前时间戳
def current_time():
    current_times = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_times
