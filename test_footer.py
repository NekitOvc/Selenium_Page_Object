from pages.main_page import MainPage

import requests

def test_footer_links(driver):
    main_page = MainPage(driver)
    main_page.go_to_site()

    footer_links = main_page.get_footer_links()
    expected_links = [
        '/user-agreement',
        '/license-agreement',
        '/confidentiality-of-personal-information',
        '/promo-codes-terms-and-conditions',
        '/about-recommendation-technologies',
        'https://docs.google.com/spreadsheets/d/1AOhpTgj2npSecsW-C7WGmOyw_rNkf571k4bHodMv_RU/edit',
        '/trademarks'
    ]

    expected_links_texts = [
        'Пользовательское соглашение',
        'Лицензионное соглашение',
        'Политика обработки персональных данных',
        'Условия применения промокодов',
        'О рекомендательных технологиях',
        'Полное меню',
        'Товарные знаки'
    ]

    for i, link in enumerate(footer_links):
        url = link.get_attribute("href")
        link_text = link.text
        assert url.endswith(expected_links[i])
        assert link_text == expected_links_texts[i]

        if not url.startswith("https://docs.google.com"):
            response = requests.get(url)
            assert response.ok

def test_payment_logos(driver):
    main_page = MainPage(driver)
    main_page.go_to_site()

    payment_logos = main_page.get_payment_logos()
    expected_logos = [
        "/files/images/logo-mastercard_small.svg",
        "/files/images/logo-visa_small.svg",
        "/files/images/logo-mir_small.svg",
        "/files/images/logo_sbp_monochrome.svg"
    ]

    for i, logo in enumerate(payment_logos):
        assert logo.get_attribute("src").endswith(expected_logos[i])

def test_copyright(driver):
    main_page = MainPage(driver)
    main_page.go_to_site()
    copyright = main_page.get_copyright()
    assert copyright == "©2024, Dostaevsky", "Copyright text is incorrect"

def test_developer_text(driver):
    main_page = MainPage(driver)
    main_page.go_to_site()
    developer_text = main_page.get_developer_text()
    assert developer_text == "Задизайнено", "Developer text is incorrect"

def test_developer_link(driver):
    main_page = MainPage(driver)
    main_page.go_to_site()
    developer_link = main_page.get_developer_link()
    assert developer_link.get_attribute('href') == "https://artu.studio/", "Developer link is incorrect"