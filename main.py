from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver import ActionChains
from datetime import datetime, timedelta


chrome_options = Options()


user_data_dir = os.path.expanduser("~/whatsapp_session")  
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")


chrome_options.add_argument("--profile-directory=Default")

chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


driver.get("https://web.whatsapp.com")

time.sleep(15)  
print("WhatsApp Web loaded!")


search_button_xpath = '//button[@aria-label="Search or start new chat"]'
search_button = driver.find_element(By.XPATH, search_button_xpath)
search_button.click()
print("Search button clicked!")


previous_day = datetime.now() - timedelta(days=1)
group_name = previous_day.strftime(f"%-d-%-m-%Y")  


search_input_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
search_input = driver.find_element(By.XPATH, search_input_xpath)


search_input.click()  
search_input.send_keys(group_name)  
search_input.send_keys(Keys.ENTER)  
print(f"Group name '{group_name}' typed and Enter pressed!")


time.sleep(2)


group_xpath = f'//span[@dir="auto" and text()="{group_name}"]'
group_element = driver.find_element(By.XPATH, group_xpath)
group_element.click()  # Click the group once found
print(f"Group '{group_name}' clicked!")
time.sleep(2)


pencil_icon_xpath = '//span[@data-icon="pencil"]'
pencil_icon = driver.find_element(By.XPATH, pencil_icon_xpath)
pencil_icon.click()
print("Pencil icon clicked to edit the group name!")


new_group_name = datetime.now().strftime(f"%-d-%-m-%Y")  

actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
actions.send_keys(new_group_name)
actions.send_keys(Keys.ENTER)
actions.perform()

print(f"Group name changed to '{new_group_name}'!")


time.sleep(2)
