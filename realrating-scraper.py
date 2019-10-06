from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


def search_url(url, content):
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--incognito")
    options.add_experimental_option("detach", True)

    browser = webdriver.Chrome(options=options)

    browser.get(url)
    # html = broswer.page_source

    search_field = browser.find_elements_by_id("navbar-query")[0]
    search_field.send_keys(content, Keys.ENTER)
    browser.get(browser.current_url)
    result_url = browser.find_elements_by_class_name(
        "result_text")[0].find_element_by_tag_name("a").click()

    # print(result_url)


def main():
    imdb_url = "https://imdb.com/"
    search_content = "Joker"

    search_url(imdb_url, search_content)


main()
