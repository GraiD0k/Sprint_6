import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем пока загрузиться элемент')
    def waiting_loading_page(self,xpath):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(xpath))


    @allure.step('Переключение на новую вкладку')
    def switch_to_new_tab(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    @allure.step('Проверка адреса страницы')
    def assert_current_url(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))
        assert self.driver.current_url == url
