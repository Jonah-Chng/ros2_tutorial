#/usr/bin/env python3
import logging

def dev_main():
    logging.basicConfig(filename='log/example.log', level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')
    logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
