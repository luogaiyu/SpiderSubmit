import logging
format='%(levelname)s - %(asctime)s - %(message)s '
# 添加控制台
logger = logging.getLogger('spider')
ch = logging.StreamHandler()
file_handler = logging.FileHandler('my_log.txt')
file_handler.setFormatter(logging.Formatter(format))
file_handler.setLevel("DEBUG")
logger.addHandler(file_handler)
logger.debug('This is a debug message')
logger.error("This is a debug message")