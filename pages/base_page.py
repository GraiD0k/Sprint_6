import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
from locators.main_page_locators import MainPageLocators
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем пока загрузиться элемент')
    def waiting_loading_page(self,xpath,driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(xpath))


    @allure.step('Переключение на новую вкладку')
    def switch_to_new_tab(self,driver):
        windows = driver.window_handles
        driver.switch_to.window(windows[1])

    @allure.step('Проверка адреса страницы')
    def assert_current_url(self, url,driver):
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url))
        assert driver.current_url == url

    @allure.step('Нажимаем кнопку заказать')
    def click_button_order(self,driver):
        self.waiting_loading_page(MainPageLocators.ORDER_BUTTON_XPATH,driver)
        driver.find_element(*MainPageLocators.ORDER_BUTTON_XPATH).click()
