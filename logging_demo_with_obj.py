import logging

logging.basicConfig(filename= 'D://pythonProject//SeleniumTest//practice//log_report//log_report_with_object.log',
                    #level=logging.DEBUG,
                    )

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.info('this is info')
logger.debug("this is debug")
logger.error("this is error")
logger.warning("this is warning")
logger.critical("this is critical")

