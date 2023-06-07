from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = Options()
opts.add_argument('--start-mazimized')
opts.add_argument('--enable-automation')
opts.add_argument('--incognito')
browser = Firefox(options=opts)
browser.get('https://duckduckgo.com')
search_form = browser.find_element(By.ID, 'search_form_input_homepage')
search_form.send_keys('real python')
search_form.submit()
try:
    WebDriverWait(browser, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
except:
    browser.quit()
results = browser.find_element(By.ID, 'react-results--main')
print(results[0].text)
browser.quit()