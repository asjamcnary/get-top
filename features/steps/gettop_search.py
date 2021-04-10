from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

$x("//span[@class='section-title-main']")

$x("//img[@src='https://gettop.us/wp-content/uploads/2020/07/ªá¥ááã-àë-2.jpg']")
$x("//img[@src='https://gettop.us/wp-content/uploads/2020/07/©¯¥¤ë.jpg']")
$x("//img[@src='https://gettop.us/wp-content/uploads/2020/07/â¥«¥ä®­ë.jpg']")
$x("//img[@src='https://gettop.us/wp-content/uploads/2020/07/­®ãâë-2.jpg']")


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)