class LogLevel:
    DEBUG = 0
    INFO = 1
    WARN = 2
    ERROR = 3


class Logger:
    def __init__(self, log_lvl=LogLevel.INFO):
        self.log_lvl = log_lvl

    def log(self, msg, lvl=LogLevel.INFO):
        if lvl >= self.log_lvl:
            print(msg)

    def debug(self, msg):
        self.log(msg=msg, lvl=LogLevel.DEBUG)

    def info(self, msg):
        self.log(msg=msg, lvl=LogLevel.INFO)

    def warn(self, msg):
        self.log(msg=msg, lvl=LogLevel.WARN)

    def error(self, msg):
        self.log(msg=msg, lvl=LogLevel.ERROR)

    def always_log(self, msg):
        self.log(msg=msg, lvl=99)