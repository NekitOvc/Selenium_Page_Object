from pages.main_page import MainPage

def test_feedback_block_telegram(driver):
    main_page = MainPage(driver)
    main_page.go_to_site()
    main_page.get_header_feedback()
    assert main_page.get_header_feedback_telegram()

def test_feedback_block_whatsapp(driver):
    main_page = MainPage(driver)
    main_page.go_to_site()
    main_page.get_header_feedback()
    assert main_page.get_header_feedback_whatsapp()

def test_feedback_block_chat(driver):
    main_page = MainPage(driver)
    main_page.go_to_site()
    main_page.get_header_feedback()
    assert main_page.get_header_feedback_chat()

def test_feedback_block_contact_us(driver):
    main_page = MainPage(driver)
    main_page.go_to_site()
    main_page.get_header_feedback()
    assert main_page.get_header_feedback_contact_us()