from selenium import webdriver
from behave import when, then, given
from selenium.webdriver.common.by import By

BROWSE_OUR_CATEGORIES = (By.XPATH, "//a[@href='https://gettop.us/product-category/accessories/']")

CATEGORY_NAME_1 = (By.XPATH, "//img[@src='https://gettop.us/wp-content/uploads/2020/07/ªá¥ááã-àë-2.jpg']")
CATEGORY_NAME_2 = (By.XPATH, "//img[@src='https://gettop.us/wp-content/uploads/2020/07/©¯¥¤ë.jpg']")
CATEGORY_NAME_3 = (By.XPATH, "//img[@src='https://gettop.us/wp-content/uploads/2020/07/â¥«¥ä®­ë.jpg']")
CATEGORY_NAME_4 = (By.XPATH, "//img[@src='https://gettop.us/wp-content/uploads/2020/07/­®ãâë-2.jpg']")


@given('Open Gettop page')
def open_gettop_page(context):
    context.driver.get('https://gettop.us')

@then('"Browse Our Categories" text is shown')
def verify_browse_our_categories_present(context):
    context.driver.find_element(*BROWSE_OUR_CATEGORIES)

@then('4 {expected_categories} are shown')
def verify_categories_count(context, expected_categories):
    actual_categories = context.driver.find_elements(*EXPECTED_CATEGORIES)
    assert len(actual_categories) == int(expected_categories), f'Expected {expected_categories}'

@then('Verify correct categories names')
def correct_categories_names(context):
    correct_category = context.driver.find_elements(*CATEGORIES)
    for e in category_elements:
        assert 'category_name' in e.text, f'Error {category_names}'
        category_name = e.find_element(*CATEGORY_NAME).text
        print(category_name)
        assert category_name, f'Error {category_names}'

@then('User can click through each category name and verify correct page opens')
def click_thru_category_names(context):
    category_names = context.driver.find_elements(*CATEGORY_NAMES)

for x in range(len(category_names)):
    category = context.driver.find_elements(*CATEGORY_NAMES)[x]

    category_name_text = category_name.text
    category_name.click()

    category_name_text = context.driver.find_element(*CATEGORY).text
assert category_text in category_text, f'Expected {category_name} not in {category_text}'


driver.quit()
