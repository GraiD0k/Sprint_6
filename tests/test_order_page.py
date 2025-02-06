from pages.order_page import OrderPage
import allure
import pytest
from data.urls import Urls
from conftest import driver
from locators.order_page_locators import OrderPageLocators

class TestOrderPage:
    TEXT_SUCCES_CREATE_ORDER = 'Отменить заказ'

    @pytest.mark.parametrize ('step1, step2', [
                [{'name': 'Тестировщик', 'last_name': 'Автоматизаторов', 'address': 'Москва, Самокатная, д69', 'phone': '+79006084444'},
                {'comment': 'Комментарий для курьера номер 1'}],
                [{'name': 'Автоматизатор', 'last_name': 'Тестировщик', 'address': 'Москва, Тестовая, д6', 'phone': '+7960902020'},
                {'comment': 'Комментарий для курьера номер 2'}]] , ids =["First Order Test Case", "Second Order Test Case"])
    @allure.title('Проверка заказа самоката')
    def test_order_scooter(self, step1, step2, driver):
        driver.get(Urls.URL_BASE)
        order_page = OrderPage(driver)
        order_page.click_button_order()
        order_page.waiting_loading_page(OrderPageLocators.FIELD_NAME_XPATH)
        order_page.set_abonent_data_step1(step1['name'],step1['last_name'],step1['address'],step1['phone'])
        order_page.assert_go_next_step()
        order_page.set_abonent_data_step2(step2['comment'])
        order_page.assert_succes_create_order(self.TEXT_SUCCES_CREATE_ORDER)