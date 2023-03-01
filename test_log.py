import logging

logging.basicConfig(filename='Log/app.log', filemode='a', format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO) #%(name)s - %(levelname)s -
logging.debug('This will get logged to a file')
logging.info('This is an info message')