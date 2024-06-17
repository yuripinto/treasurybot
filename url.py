import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from product import Product

class URLProcessor:
    domain_xpath_map = {
        'www.magazineluiza.com.br': '//*[@data-testid="price-value"]',
        'www.extra.com.br': '//*[@data-testid="product-price-value"]'
    }

    @staticmethod
    def get_xpath(url):
        parsed_url = urllib.parse.urlparse(url)
        domain = parsed_url.netloc
        return URLProcessor.domain_xpath_map.get(domain, 'Unknown domain')

    @staticmethod
    def load_url_list(path):
        with open(path, 'r') as file:
            url_list = file.readlines()
        return [url.strip() for url in url_list]

    @staticmethod
    def process_url_with_selenium(url):
        options = Options()
        #options.add_argument("--headless")  # Easy to get detected as bot
        #options.add_argument("--no-sandbox")
        #options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)
        #driver.minimize_window()
        driver.get(url)

        new_product = Product(
            name=driver.title,
            price=driver.find_element(By.XPATH, URLProcessor.get_xpath(url)).text,
            url=url
        )
        driver.quit()
        return new_product