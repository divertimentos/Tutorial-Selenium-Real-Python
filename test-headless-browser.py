from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import NoSuchElementException

# try:
#     pass
# except NoSuchElementException as e:
#     print(e)

# Creating a headless browser:
opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
browser = Chrome(options=opts)
browser.get('https://duckduckgo.com')


# Querying the DOM
search_form = browser.find_element_by_id('search_form_input_homepage')
search_form.send_keys('real python')
search_form.submit()


# Printing the results:
results = browser.find_elements_by_class_name('result')
print(results[0].text)

browser.close()
quit()