import logging
import time
import random
from product import Product
from url import URLProcessor
#from rocketry import Rocketry

#app = Rocketry()

#@app.task('every 5 minute')
def start_crawler():
    logging.info('Reading url list from file')
    url_list = URLProcessor.load_url_list('urls.txt')
    for url in url_list:
        logging.info(f"Processing URL: {url}")
        new_product = URLProcessor.process_url_with_selenium(url)
        new_product.save()
        logging.info(f"Record saved: {new_product.name}, {new_product.price}")
        logging.info(f"Cooldown")
        time.sleep(random.uniform(1, 3))

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    start_crawler()
    #app.run()