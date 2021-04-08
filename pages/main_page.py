from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    BROWSE_OUR_CATEGORIES = (By.XPATH, "//a[@href='https://gettop.us/product-category/accessories/']")

    CATEGORY_NAME_1 = (By.XPATH, "//img[@src='https://gettop.us/wp-content/uploads/2020/07/ªá¥ááã-àë-2.jpg']")
    CATEGORY_NAME_2 = (By.XPATH, "//img[@src='https://gettop.us/wp-content/uploads/2020/07/©¯¥¤ë.jpg']")
    CATEGORY_NAME_3 = (By.XPATH, "//img[@src='https://gettop.us/wp-content/uploads/2020/07/â¥«¥ä®­ë.jpg']")
    CATEGORY_NAME_4 = (By.XPATH, "//img[@src='https://gettop.us/wp-content/uploads/2020/07/­®ãâë-2.jpg']")

    def open_main_page(self):
        self.open_url()

    def verify_browse_our_categories_present(self):
        self.driver.find_element(*BROWSE_OUR_CATEGORIES)

    def verify_categories_count(self, expected_categories):
        actual_categories = self.driver.find_elements(*EXPECTED_CATEGORIES)
        assert len(actual_categories) == int(expected_categories), f'Expected {expected_categories}'

    def correct_categories_names(self):
        correct_category = self.driver.find_elements(*CATEGORIES)
        for e in category_elements:
            assert 'correct_category_name' in e.text, f'Error {category_names}...'
            category_name = e.find_element(*CATEGORY_NAME).text
            print(category_name)
            assert category_name, f'Error {category_names}'

    def click_thru_category_names(self):
        category_names = self.driver.find_elements(*CATEGORY_NAMES)

    for x in range(len(category_names)):
        category = self.driver.find_elements(*CATEGORY_NAMES)[x]

        category_name_text = category_name.text
        category_name.click()

        category_name_text = self.driver.find_element(*CATEGORY).text
    assert category_text in category_text, f'Expected {category_name} not in {category_text}'




















