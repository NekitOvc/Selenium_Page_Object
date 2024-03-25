from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Locators:
    CATEGORY = (By.XPATH, '//div[@class="category"]')
    BANNER_NEXT_BUTTON = (By.XPATH, '//div[@class="swiper-button-next swiper-button-white"]')
    BANNER_PREVIOUS_BUTTON = (By.XPATH, '//div[@class="swiper-button-prev swiper-button-white"]')
    BANNER_BUTTON = (By.XPATH, '//img[@title="Подарок в приложении СПБ"]')
    SEO_TEXT = (By.XPATH, '//div[@class="seo"]')
    MAIN_CATEGORY_LIST = (By.XPATH, '//a[@class="main-nav__link"]')
    MAIN_CATEGORY_LIST_PANEL = (By.XPATH, '//div[@class="category__content"]')

    HEADER_FEEDBACK = (By.XPATH, '//div[@class="header__contactus contact-us "]')
    HEADER_FEEDBACK_TELEGRAM = (By.XPATH, '//a[@href="https://t.me/Dostahelp_bot"]')
    HEADER_FEEDBACK_WHATSAPP = (By.XPATH, '//a[@href="https://api.whatsapp.com/send?phone=78127778008"]')
    HEADER_FEEDBACK_CHAT = (By.XPATH, '//a[@href="javascript:void(0);"]')
    HEADER_FEEDBACK_CONTACT_US = (By.XPATH, '//a[text()="Обратный звонок"]')

    FOOTER_LINKS = (By.XPATH, '//a[@class="footer-link__link"]')
    PAYMENT_LOGOS = (By.XPATH, '//li[@class="payments-system__logo"]/img')
    COPYRIGHT = (By.XPATH, '//div[@class="footer__copyright"]/span')
    DEVELOPER_TEXT = (By.XPATH, '//span[text()="Задизайнено "]')
    DEVELOPER_LINK = (By.XPATH, '//a[@href="https://artu.studio/"]')


class MainPage(BasePage):
    def search_category(self):
        return self.element_is_visible(Locators.CATEGORY)
    
    def banner_next_button(self):
        return self.element_is_visible(Locators.BANNER_NEXT_BUTTON)
    
    def banner_previous_button(self):
        return self.element_is_visible(Locators.BANNER_PREVIOUS_BUTTON)
    
    def banner_button(self):
        return self.element_is_visible(Locators.BANNER_BUTTON)
    
    def seo_text(self):
        return self.element_is_visible(Locators.SEO_TEXT)
    
    def main_category_navigation_panel_list(self):
        return self.find_elements(Locators.MAIN_CATEGORY_LIST)
    
    def category_main_page_list(self):
        return self.find_elements(Locators.MAIN_CATEGORY_LIST_PANEL)
    
    def get_header_feedback(self):
        header_feedback = self.element_is_visible(Locators.HEADER_FEEDBACK)
        header_feedback.click()

    def get_header_feedback_telegram(self):
        return self.element_is_visible(Locators.HEADER_FEEDBACK_TELEGRAM)
    
    def get_header_feedback_whatsapp(self):
        return self.element_is_visible(Locators.HEADER_FEEDBACK_WHATSAPP)
    
    def get_header_feedback_chat(self):
        return self.element_is_visible(Locators.HEADER_FEEDBACK_CHAT)
    
    def get_header_feedback_contact_us(self):
        return self.element_is_visible(Locators.HEADER_FEEDBACK_CONTACT_US)
    
    def get_footer_links(self):
        return self.find_elements(Locators.FOOTER_LINKS)
    
    def get_payment_logos(self):
        return self.find_elements(Locators.PAYMENT_LOGOS)

    def get_copyright(self):
        return self.find_element(Locators.COPYRIGHT).text

    def get_developer_text(self):
        return self.find_element(Locators.DEVELOPER_TEXT).text

    def get_developer_link(self):
        return self.find_element(Locators.DEVELOPER_LINK)
