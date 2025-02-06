import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from conftest import driver
class MainPage(BasePage):
    @allure.step('Нажатие на вопрос')
    def click_question(self, xpath, driver):
        driver.find_element(*xpath).click()
    @allure.step('Получение ответа на вопрос')
    def receiving_text_answer (self,xpath_text_, driver):
        return driver.find_element(*xpath_text_).text
    @allure.step('Сравниваем ответ на вопрос')
    def check_text_answers(self, xpath ,xpath_text,answer_text, driver):
        self.waiting_loading_page(xpath,driver)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.waiting_loading_page(xpath,driver)
        self.click_question(xpath,driver)
        assert self.receiving_text_answer(xpath_text,driver) == answer_text

    @allure.step('Нажатие на логотип "Самоката"')
    def click_scooter_logo(self, driver):
        driver.find_element(*MainPageLocators.LOGO_SCOOTER_XPATH).click()

    @allure.step('Нажатие на логотип "Яндекс"')
    def click_yandex_logo(self, driver):
        self.waiting_loading_page(MainPageLocators.LOGO_YANDEX_XPATH)
        driver.find_element(*MainPageLocators.LOGO_YANDEX_XPATH).click()