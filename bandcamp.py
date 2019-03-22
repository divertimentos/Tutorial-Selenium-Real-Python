from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import NoSuchElementException

opts = Options()
opts.set_headless()
browser = Chrome(options=opts)
browser.get('https://bandcamp.com')
browser.find_element_by_class_name('playbutton').click()

