from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from sys import exit

# Account credentials.
EMAIL = "<EMAIL>"
PASSWORD = "<PASSWORD>"

# URLs to work with
LOGIN_URL = "https://www.linkedin.com/uas/login"

# Person to like latest post from
PROFILE_NAME = "Israel Kehat"

class LinkedInAccount(object):
    def __init__(self):
        super(LinkedInAccount, self).__init__()
        self.driver = webdriver.Chrome()

    def sign_in(self, login_url, email, password):
        print("Going to sign in page...")
        self.driver.get(login_url)

        print("Typing credentials...")
        input_email = self.driver.find_element(By.XPATH, "//input[@name='session_key']")
        input_email.clear()
        input_email.send_keys(email)

        input_password = self.driver.find_element(By.XPATH, "//input[@name='session_password']")
        input_password.clear()
        input_password.send_keys(password)

        submit_login_btn = self.driver.find_element(By.XPATH, "//input[@type='submit'] | //button[@type='submit']")
        submit_login_btn.click()
    
        print("Successfully signed in...")

    def wait_and_get_component(self, xpath_pattern, delay):
        return WebDriverWait(self.driver, delay)\
                .until(EC.presence_of_element_located((By.XPATH, xpath_pattern)))

    def search_profile(self, profile_name):
        print("Searching profile...")
        search_field = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        search_field.send_keys(profile_name + Keys.ENTER)

        try:
            best_match = self.wait_and_get_component("(//a[@data-control-name='search_srp_result'])[1]", 15)
            best_match.click()
            print("Navigating to profile...")
        except TimeoutException as te:
            print("The page took too much time to load...\n-- FINISHED --")
            self.driver.close()
            exit(0)

    def navigate_to_recent_activity(self):
        print("Navigating to recent activity...")

        try:
            recent_activity = self.wait_and_get_component("//a[@data-control-name='recent_activity_details_all']", 15)
            recent_activity.click()
        except TimeoutException as te:
            print("The page took too much time to load...\n-- FINISHED --")
            self.driver.close()
            exit(0)

    def like_latest_post(self):
        print("Evaluating last post...")

        try:
            latest_like_button = self.wait_and_get_component("(//button[@data-control-name='like_toggle'])[1]", 15)
            isLiked = True if latest_like_button.find_element(By.XPATH, ".//span[@class='visually-hidden']").text == "Unlike" else False
            if isLiked:
                print("The last post has already been liked.")
            else: 
                latest_like_button.click() 
                print("The last post has been liked.")
        except TimeoutException as te:
            print("The page took too much time to load...\n-- FINISHED --")
            self.driver.close()
            exit(0)

def main():
    print("-- STARTING BROWSER --")

    account = LinkedInAccount()
    account.sign_in(LOGIN_URL, EMAIL, PASSWORD)
    account.search_profile(PROFILE_NAME)
    account.navigate_to_recent_activity()
    account.like_latest_post()

    print("-- FINISHED --")
    sleep(3) # Sleeps for 3 seconds...

if __name__ == '__main__':
    main()
