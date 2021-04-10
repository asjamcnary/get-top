from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):


    HEADER = (By.XPATH, "//span[@class='section-title-main']")
    HEADER_TITLE = (By.XPATH, "//a[@href='https://gettop.us/product-category']")


    def open_main_page(self):
        self.open_url()

    def verify_browse_our_categories_present(self):
        self.driver.find_element(*HEADER)

    def verify_categories_count(self, expected_titles):
        actual_titles = self.driver.find_elements(*EXPECTED_TITLES)
        assert len(actual_titles) == int(expected_titles), f'Expected {expected_titles}'

    def correct_category_links(self):
        correct_header_title = self.driver.find_elements(*TITLES)
        for e in header_elements:
            assert 'correct_header_titles' in e.text, f'Error {header_titles}'
            header_title = e.find_element(*HEADER_TITLE).text
            print(header_title)
            assert header_title, f'Error {header_titles}'

    def click_thru_category_links(self):
        header_titles = self.driver.find_elements(*HEADER_TITLES)

    for x in range(len(header_titles)):
        category = self.driver.find_elements(*CATEGHEADER_TITLE)[x]

        header_title_text = header_title.text
        header_title.click()

        header_title_text = self.driver.find_element(*HEADER).text
    assert header_title in header_text, f'Expected {header_title} not in {header_text}'






















