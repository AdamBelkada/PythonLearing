
import logging
import os
import datetime as dt
import sys

# The logger is created here so that the entire module can reference it without passing it around.
logger = logging.getLogger("")
"""
 levels:
 critical   50
 error      40
 warning    30
 info       20
 debug      10
"""
#by default it disply from warning
#changing to have all messages
#this is just a way of recording error types
# logging.debug("This is a warning msg")
# logging.info("This is a info msg")
# logging.warning("This is a warning msg")
# logging.error("This is a error msg")
# logging.critical("This is a critical msg")

def logger_initialize():
    """ Initializes the logger declared at the module level. This is still required. Otherwise, the log entries would just get suppressed. """
    logger.setLevel(logging.DEBUG)
    message_format = "{asctime} | {levelname:<8} | {name} | {message}"
    date_format    = "%Y-%m-%d %H:%M:%S"
    format_style   = "{"
    universal_formatter = logging.Formatter(fmt = message_format, datefmt = date_format, style = format_style)
    time_stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = os.path.join(os.path.dirname(__file__), "logs", time_stamp + "_logfile.log")
    
    #Log file output
    file_handler = logging.FileHandler(file_name)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(universal_formatter)
    logger.addHandler(file_handler)    

    # Terminal output
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(universal_formatter)
    logger.addHandler(console_handler)

    """
    Also you can use basicConfig
    # time_stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    # logger.basicConfig (
    # level = logging.CRITICAL,
    # format= "{asctime} | {levelname:<8} | {name} | {message}",
    # style ='{',
    # filename = os.path.join(os.path.dirname(__file__), "logs", time_stamp + "_mylog.log"),
    #filemode = 'w' it's not needed here because it's creating a new log for every execution
    """
    logger.info("Log initialized.")
    return logger




def main():
    username = "Adam.Belkada"
    logger = logger_initialize()
    logger.info(f"This is a  message with user: {username}")
    try:
        a = 2
        b = 1
        c = a/b
        print (c)
    except Exception as e:
        logger.exception(e)
        raise e
    else:
        print("commit changes because no exception")
        logger.info(f"finished message from user:{username}")
    finally:
        print ("here where you close connetion for example, this run whether there is an exception or not")


    while True:
        try:
            x = int (input("Please enter a number: "))
            break
        except ValueError:
            logger.info("Oops!that was no valid number. Try again...")

if __name__ == "__main__":
    main()