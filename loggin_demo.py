import logging

logging.basicConfig(filename="D://pythonProject//SeleniumTest//practice//log_report//log_report.log",
                    #format="% (asctime)s: % (levelname)s: %(message)s",
                    #datefmt="%d%m%Y %i:%m%s %p",
                    level=logging.DEBUG
                    )


logging.info('this is info')
logging.debug("this is debug")
logging.error("this is error")
logging.warning("this is warning")
logging.critical("this is critical")
