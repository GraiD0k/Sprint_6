import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):
    @allure.step('Ожидаем формы для оформления заказа')
    def loading_page_order(self,driver):
        self.waiting_loading_page(OrderPageLocators.FIELD_NAME_XPATH,driver)
    @allure.step('Вводим Имя')
    def set_name(self,name,driver):
        driver.find_element(*OrderPageLocators.FIELD_NAME_XPATH).send_keys(name)

    @allure.step('Вводим фамилию')
    def set_last_name(self,last_name,driver):
        driver.find_element(*OrderPageLocators.FIELD_FAMILY_XPATH).send_keys(last_name)

    @allure.step('Вводим Адрес')
    def set_address(self,address,driver):
        driver.find_element(*OrderPageLocators.FIELD_ADDRESS_XPATH).send_keys(address)

    @allure.step('Выбираем странцию метро')
    def click_metro_station(self,driver):
        driver.find_element(*OrderPageLocators.FIELD_METRO_XPATH).click()
        self.waiting_loading_page(OrderPageLocators.DROPDOWN_METRO_XPATH,driver)
        driver.find_element(*OrderPageLocators.DROPDOWN_METRO_XPATH).click()

    @allure.step('Вводим телефон')
    def set_phone(self,phone,driver):
        driver.find_element(*OrderPageLocators.FIELD_PHONE_NUMBER_XPATH).send_keys(phone)

    @allure.step('Нажимаем кнопку далее')
    def click_button_next(self,driver):
        driver.find_element(*OrderPageLocators.NEXT_BUTTON_XPATH).click()

    def set_abonent_data_step1(self,name,last_name,address,phone,driver):
        self.set_name(name,driver)
        self.set_last_name(last_name,driver)
        self.set_address(address,driver)
        self.click_metro_station(driver)
        self.set_phone(phone,driver)
        self.click_button_next(driver)
        self.waiting_loading_page(OrderPageLocators.TEXT_ABOUT_RENT_XPATH,driver)

    @allure.step('Проверка, что перешли на второй шаг заказа')
    def assert_go_next_step(self,driver):
        assert 'Про аренду' == driver.find_element(*OrderPageLocators.TEXT_ABOUT_RENT_XPATH).text

    @allure.step('Выбираем когда привезти самокат')
    def set_data(self,driver):
        driver.find_element(*OrderPageLocators.FIELD_WHEN_BRING_SCOOTER_XPATH).click()
        driver.find_element(*OrderPageLocators.DATA_FOR_ORDER_XPATH).click()

    @allure.step('Выбираем срок аренды')
    def set_rental_period(self,driver):
        driver.find_element(*OrderPageLocators.FIELD_RENTAL_PERIOD_XPATH).click()
        self.waiting_loading_page(OrderPageLocators.DROPDOWN_RENTAL_PERIOD_XPATH,driver)
        driver.find_element(*OrderPageLocators.DROPDOWN_RENTAL_PERIOD_XPATH).click()

    @allure.step('Выбираем чек-бокс цвет самоката')
    def set_checkbox_color_scooter(self,driver):
        driver.find_element(*OrderPageLocators.CHECKBOX_COLOR_SCOOTER_XPATH).click()

    @allure.step('Вводим комментарий для курьера')
    def set_comment(self,comment,driver):
        driver.find_element(*OrderPageLocators.FIELD_COMMENT_FOR_COURIER_XPATH).send_keys(comment)

    @allure.step('Нажимаем кнопку заказать')
    def click_order_scooter(self,driver):
        driver.find_element(*OrderPageLocators.BUTTON_ORDER_XPATH).click()


    @allure.step('Подтверждаем оформление заказа')
    def click_yes_for_popup_do_you_want_place_order(self,driver):
        self.waiting_loading_page(OrderPageLocators.BUTTON_YES_FOR_POPUP_XPATH,driver)
        driver.find_element(*OrderPageLocators.BUTTON_YES_FOR_POPUP_XPATH).click()

    @allure.step('Нажимаем на кнопку посмотреть статус')
    def click_watch_status(self,driver):
        driver.find_element(*OrderPageLocators.BUTTON_WATCH_STATUS_XPATH).click()

    @allure.step('Получаем текст с фронта о отмене заказа')
    def get_text_for_front(self,locator,driver):
        return driver.find_element(*locator).text

    @allure.step('Сравниваем текст с тем что на фронте')
    def assert_succes_create_order(self, text_for_popup):
        assert text_for_popup == self.get_text_for_front(OrderPageLocators.BUTTON_ORDER_CANCEL_XPATH)

    def set_abonent_data_step2(self,comment,driver):
        self.set_data(driver)
        self.set_rental_period(driver)
        self.set_checkbox_color_scooter(driver)
        self.set_comment(comment,driver)
        self.click_order_scooter(driver)
        self.click_yes_for_popup_do_you_want_place_order(driver)
        self.waiting_loading_page(OrderPageLocators.ORDER_REGISTER_XPATH,driver)
        self.waiting_loading_page(OrderPageLocators.BUTTON_WATCH_STATUS_XPATH,driver)
        self.click_watch_status(driver)
        self.waiting_loading_page(OrderPageLocators.BUTTON_ORDER_CANCEL_XPATH,driver)
