def main():

    # logging.MyFileHandler = MyFileHandler
    # logging.MyTimeRotatingFileHandler = MyTimeRotatingFileHandler

    # logging.setup(CONF, "test")
    # Log = logging.getLogger("debug")

    Log = Logger("debug")
    Log.debug("log info")
    Log.info("root info")
    Log.warning("Warning info")
    Log.error("log")


if __name__ == "__main__":

    from src.utils.logger import *
    main()
