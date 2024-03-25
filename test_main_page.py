from pages.main_page import MainPage

def test_main_page(driver):
    main_page = MainPage(driver)
    main_page.go_to_site()
    main_page.banner_next_button()
    main_page.banner_next_button()
    main_page.banner_previous_button()
    assert main_page.banner_button()

def test_seo_text(driver):
    main_page = MainPage(driver)
    main_page.go_to_site()
    assert main_page.seo_text()

def test_navigation_list(driver):
    main_page = MainPage(driver)
    main_page.go_to_site()

    elements_navigation_panel = main_page.main_category_navigation_panel_list()
    category_navigation_panel_list = []
    for element_navigation_panel in elements_navigation_panel:
        category_navigation_panel_list.append(element_navigation_panel.text)

    elements_main_page = main_page.category_main_page_list()
    category_main_page_list = []
    for element_main_page in elements_main_page:
        category_main_page_list.append(element_main_page.text)

    assert category_navigation_panel_list == category_main_page_list