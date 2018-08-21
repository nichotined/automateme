import os
import logzero


class Logger:
    def __init__(self, name="MobileAutomation"):
        self.name = name
        self.logfile = "/tmp/{0}.log".format(self.name)
        self.delete_log()

    def initialize(self):
        return logzero.setup_logger(name=self.name, logfile=self.logfile, formatter=Formatter.simple())

    def delete_log(self):
        try:
            os.remove(self.logfile)
        except (FileNotFoundError, FileExistsError) as e:
            print(e)


class Formatter:
    @staticmethod
    def simple():
        formatter = '%(color)s[%(levelname)1.1s]%(end_color)s ' \
                    '%(color)s[%(message)s]%(end_color)s ' \
                    '%(color)s[%(asctime)s]%(end_color)s'
        log_zero_formatter = logzero.LogFormatter(fmt=formatter)
        return log_zero_formatter
