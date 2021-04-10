from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):


    HEADER = (By.XPATH, "//span[@class='section-title-main']")
    HEADER_TITLE = (By.XPATH, "//a[@href='https://gettop.us/product-category']")


    def open_main_page(self):
        self.open_url()

    def verify_header_present(self):
        self.driver.find_element(*HEADER)

    def verify_header_titles_count(self, expected_header_titles):
        actual_header_titles = self.driver.find_elements(*EXPECTED_HEADER-TITLES)
        assert len(actual_header_titles) == int(expected_header_titles), f'Expected {expected_header_titles}'

    def correct_header_titles(self):
        correct_header_title = self.driver.find_elements(*HEADER_TITLES)
        for e in header_title_elements:
            assert 'header_titles_name' in e.text, f'Error {header_titles}'
            header_title_name = e.find_element(*HEADER_TITLE).text
            print(header_title_name)
            assert header_title_name, f'Error {header_title_names}'

    def click_thru_header_titles-names(self):
        header_title_names = self.driver.find_elements(*HEADER_TITLES)

    for x in range(len(header_title_names)):
        category = self.driver.find_elements(*HEADER_TITLES)[x]

        header_title_text = header_title.text
        header_title_name.click()

        header_title_name_text = self.driver.find_element(*HEADER_TITLE).text
    assert header_title_text in header_title_text, f'Expected {header_title_name} not in {header_title_text}'






















