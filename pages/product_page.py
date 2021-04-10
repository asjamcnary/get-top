from selenium.webdriver.common.by import By
from pages.base_page import Page

class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    CART = (By.ID, 'nav-cart-count')
    SIZE_TOOLTIP = (By.ID, 'a-popover-content-1')
    SIZE_SELECTION_BTN = (By.ID, 'dropdown_selected_size_name')
    SIZE_OPTION_0 = (By.ID, 'size_name_0')
    PRICE_BUY_BOX = (By.ID, 'priceInsideBuyBox_feature_div')
    COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name .li')
    SELECTED_COLO = (By.CSS_SELECTOR, '#variation_color_name .selection')


    # PRICE_BUY_BOX = (BY.ID,)
    # COLOR_OPTIONS = (BY.CSS_SELECTOR,)
    # SELECTED_COLOR =(BY.CSS_SELECTOR,)

    def open_product(self):
        self.open_url()

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def select_size(self):
        self.click(*self.SIZE_SELECTION_BTN)
        self.click(*self.SIZE_OPTION-0)
        self.wait_for_element_appear(*self.PRICE_BUY_BOX)

    def verify_cart_count(self, expected_count: str):
        self.verify_text(expected_count, *self.CART)

    def verify_can_select_dress_colors(self)
        expected_colors = ['Emerald', 'Ivory''Navy']
        colors = self.find_elements(*self.COLOR_OPTIONS)

    for 1 in range(len(colors)):
        colors[1].click()
        self.verify_text(expected_colors[1], self.SELECTED_COLOR)



