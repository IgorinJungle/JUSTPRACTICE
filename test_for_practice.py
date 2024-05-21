import os
import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument("--headless")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
action = ActionChains(driver)
wait = WebDriverWait(driver, 15, poll_frequency=1)


@pytest.fixture()
def startANDend(scope="session"):
    driver.maximize_window()
    print("TEST STARTING")
    yield
    print("TEST FINISHED")



@allure.feature("Inputs")
def test_inputs(startANDend):
    driver.get("https://testautomationpractice.blogspot.com/")
    name = ("xpath", '//input[@id = "name"]')
    email = ("xpath", '//input[@id = "email"]')
    phone = ("xpath", '//input[@id = "phone"]')
    adres = ("xpath", '//textarea[@id = "textarea"]')

    # ACTION
    with allure.step("Name Input"):
        name_fill = driver.find_element(*name).send_keys("My Name")
    with allure.step("Email Input"):
        email_fill = driver.find_element(*email).send_keys("MYMAIL@mail.com")
    with allure.step("Phone_fill_input"):
        phone_fill = driver.find_element(*phone).send_keys("+7800 555 35 35")
    with allure.step("adress_fill_input"):
        adres_fill = driver.find_element(*adres).send_keys("Moscow, Pushkin St, 13, 27")


@allure.feature("redio buttons")
def test_radio():
    driver.get("https://testautomationpractice.blogspot.com/")

    male = driver.find_element('xpath', '//input[@id = "male"]')

    with allure.step("Click_male_button"):
        male.click()

    radio = driver.find_element('xpath', '//input[@id = "tuesday"]')

    with allure.step("Second_radio_button_click"):
        radio.click()



def test_select():
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.execute_script("window.scrollTo(0,1200)")

    sel1 = Select(driver.find_element("xpath", '//select[@id = "country"]'))
    sel1.select_by_visible_text("China")


    sel2 = Select(driver.find_element("xpath", '//select[@id = "colors"]'))
    sel2.select_by_index(2)
    date = driver.find_element("xpath", '//input[@id="datepicker"]')
    date.send_keys("12/11/2007")
    date.send_keys(Keys.ENTER)



def test_pagination():
    driver.get("https://testautomationpractice.blogspot.com/")
    select_two = driver.find_element("xpath", '(//a[text() = "2"])[1]')
    select_two.click()
    checkbox_two = driver.find_element("xpath", '(//input[@type = "checkbox"])[12]')
    checkbox_two.click()



# def test_tabs():
#     driver.get("https://testautomationpractice.blogspot.com/")
#     input_field = driver.find_element("xpath", '//input[@id = "Wikipedia1_wikipedia-search-input"]')
#     input_field.send_keys("Siemens")
#     input_field.send_keys(Keys.ENTER)
#     Siemens = driver.find_element("xpath", '//a[text() = "Siemens"]')
#     Siemens.click()
#     windows_before = driver.window_handles
#     wait.until(EC.new_window_is_opened(windows_before))
#
#     driver.switch_to.window(windows_before[1])
#     driver.close()
#     after_handles = driver.window_handles
#     driver.switch_to.window(after_handles[0])



def test_tabs_second():
    driver.get("https://testautomationpractice.blogspot.com/")
    Window_button = driver.find_element("xpath", '//button[text() = "New Browser Window"]')
    Window_button.click()


    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    driver.close()


    handles_after = driver.window_handles
    driver.switch_to.window(handles_after[0])



def test_alert():

        driver.get("https://testautomationpractice.blogspot.com/")
        confirm_alert = driver.find_element('xpath', '//button[text() = "Alert"]')
        confirm_alert.click()
        alert = wait.until(EC.alert_is_present())
        driver.switch_to.alert
        alert.accept()
        time.sleep(1)

        dismiss_alert = driver.find_element("xpath", '//button[text() = "Confirm Box"]')
        dismiss_alert.click()
        driver.switch_to.alert
        alert.dismiss()
        time.sleep(1)

        prompt_alert = driver.find_element('xpath', '//button[text() = "Prompt"]')
        prompt_alert.click()
        driver.switch_to.alert
        alert.send_keys("HELLLLLLLO!!!!!!!!!!!!!!")
        alert.accept()
        time.sleep(1)




# def test_chains():
#     driver.get("https://testautomationpractice.blogspot.com/")
#     driver.execute_script("window.scrollTo(0, 2000)")
#
#     copy_button = driver.find_element('xpath', '//button[text() = "Copy Text"]')
#     draggable = driver.find_element('xpath', '//div[@id = "draggable"]')
#     droppable = driver.find_element('xpath', '//div[@id = "droppable"]')
#     slider = driver.find_element('xpath', '//div[@id = "slider"]')
#     resizable = ('xpath', '(//div[@style = "z-index: 90;"])[3]')
#     RESIZABLE_BOX_perform = driver.find_element(*resizable)
#
#     action.double_click(copy_button).pause(1)\
#     .drag_and_drop(draggable, droppable).pause(1).perform()
#
#     driver.execute_script("window.scrollTo(0,2000)")
#     action.drag_and_drop_by_offset(slider, 180, 0).pause(1)\
#         .click_and_hold(RESIZABLE_BOX_perform).move_by_offset(150, 150).release().perform()
#
#     time.sleep(2)

def test_cookies():
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.add_cookie(
        {"name": "Vasya",
         "value": "syelCookie"}
    )

    whatCookie = driver.get_cookies()
    print(whatCookie)
    time.sleep(8)

    driver.delete_all_cookies()
    time.sleep(10)
