from config.settings import Settings
import logging


class Log:
    def __init__(self):
        logging.basicConfig(
            filename=Settings.LOG_FILE,
            filemode='a',
            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
            datefmt='%H:%M:%S',
            level=logging.WARNING
            # level=logging.DEBUG
        )

    @classmethod
    def write(self, message):
        self.__init__(self)
        logging.warning(message) #should be the same as 'level' in config
        return "Writeen!"
