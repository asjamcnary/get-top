from pages.gettop_browse_cat import MainPage
from pages.product_page import ProductPage
from pages.search_results_page import SearchResultsPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.result_page = SearchResultsPage(self.driver)
