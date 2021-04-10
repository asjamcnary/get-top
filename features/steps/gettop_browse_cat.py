from selenium import webdriver
from behave import when, then, given
from selenium.webdriver.common.by import By

HEADER = (By.XPATH, "//span[@class='section-title-main']")
HEADER_TITLE = (By.XPATH, "//a[@href='https://gettop.us/product-category']")


@given('Open Gettop page')
def open_gettop_page(context):
    context.driver.get('https://gettop.us')

@then('"Browse Our Categories" text is shown')
def verify_header_present(context):
    context.driver.find_element(*HEADER)

@then('4 {expected_header_titles} are shown')
def verify_header_titles_count(context, expected_header_titles):
    actual_header_titles = context.driver.find_elements(*EXPECTED_HEADER_TITLES)
    assert len(actual_header_titles) == int(expected_header_titles), f'Expected {expected_header_titles}'

@then('Verify correct header_titles')
def correct_header_titles(context):
    correct_header_title = context.driver.find_elements(*HEADER_TITLES)
    for e in header_title_elements:
        assert 'header_titles_name' in e.text, f'Error {header_titles}'
        header_title_name = e.find_element(*HEADER_TITLE).text
        print(header_title_name)
        assert header_title_name, f'Error {header_title_names}'

@then('User can click through each header_title name and verify correct page opens')
def click_thru_header_title_names(context):
    header_title_names = context.driver.find_elements(*HEADER_TITLES)

for x in range(len(header_title_names)):
    header_title = context.driver.find_elements(*HEADER_TITLE_NAMES)[x]

    header_title_text = header_title_name.text
    header_title_name.click()

    header_title_name_text = context.driver.find_element(*HEADER_TITLE).text
assert header_title_text in header_title_text, f'Expected {header_title_name} not in {header_title_text}'


driver.quit()
