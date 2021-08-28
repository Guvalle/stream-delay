from datetime import datetime
from datetime import timedelta

class logger:

    def write_log (content):
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%dT%H:%M:%SZ")
        log_f = open("log.txt","a+")
        log_f.write(dt_string + " - " + content + "\n")
        log_f.close()
        return