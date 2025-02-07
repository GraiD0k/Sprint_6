from conftest import driver
import allure
import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from  data.data import MainPageData
from data.urls import Urls


class TestMainPage:

    @pytest.mark.parametrize('xpath, xpath_text, answer_text',
                              [[MainPageLocators.FIRST_QUESTION_XPATH,MainPageLocators.FIRST_ANSWER_XPATH,MainPageData.FIRST_ANSWER_TEXT],
                              [MainPageLocators.SECOND_QUESTION_XPATH,MainPageLocators.SECOND_ANSWER_XPATH,MainPageData.SECOND_ANSWER_TEXT],
                              [MainPageLocators.THIRD_QUESTION_XPATH,MainPageLocators.THIRD_ANSWER_XPATH,MainPageData.THIRD_ANSWER_TEXT],
                              [MainPageLocators.FOURTH_QUESTION_XPATH,MainPageLocators.FOURTH_ANSWER_XPATH,MainPageData.FOURTH_ANSWER_TEXT],
                              [MainPageLocators.FIFTH_QUESTION_XPATH,MainPageLocators.FIFTH_ANSWER_XPATH,MainPageData.FIFTH_ANSWER_TEXT],
                              [MainPageLocators.SIXTH_QUESTION_XPATH,MainPageLocators.SIXTH_ANSWER_XPATH,MainPageData.SIXTH_ANSWER_TEXT],
                              [MainPageLocators.SEVENTH_QUESTION_XPATH,MainPageLocators.SEVENTH_ANSWER_XPATH,MainPageData.SEVENTH_ANSWER_TEXT],
                              [MainPageLocators.EIGHTH_QUESTION_XPATH,MainPageLocators.EIGHTH_ANSWER_XPATH,MainPageData.EIGHTH_ANSWER_TEXT]],
                              ids =["First Question Test Case", "Second Question Test Case","Third Question Test Case","Fourth Question Test Case","Fifth Question Test Case","Sixth Question Test Case","Seventh Question Test Case","Eighth Question Test Case"])

    @allure.title('Проверка ответа при клике на вопрос')
    def test_check_text_answer(self, xpath, xpath_text, answer_text,driver):
        main_page = MainPage(driver)
        main_page.create_main_driver(Urls.URL_BASE)
        main_page.check_text_answers(xpath, xpath_text, answer_text)

    @allure.title('Проверка перехода на главную страницу Самоката')
    def test_check_go_home(self, driver):
        main_page = MainPage(driver)
        main_page.create_main_driver(Urls.URL_BASE)
        main_page.click_button_order()
        main_page.click_scooter_logo()
        main_page.assert_current_url(Urls.URL_BASE)

    @allure.title('Проверка перехода с главной главную страницу Дзена')
    def test_passage_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.create_main_driver(Urls.URL_BASE)
        main_page.click_yandex_logo()
        main_page.switch_to_new_tab()
        main_page.assert_current_url(Urls.URL_DZEN)