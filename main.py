from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Account credentials.
EMAIL = "<EMAIL>"
PASSWORD = "<PASSWORD>"

# URLs to work with
LOGIN_URL = "https://www.linkedin.com/uas/login"
PROFILE_ACTIVITY_URL = "https://www.linkedin.com/in/ikehat/detail/recent-activity/"

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

    def like_latest_post(self, activity_url):
        print("Going to recent activity page...")
        self.driver.get(activity_url)

        print("Evaluating last post...")
        latest_like_button = self.driver.find_element(By.XPATH, "(//button[@data-control-name='like_toggle'])[1]")
        isLiked = True if latest_like_button.find_element(By.XPATH, ".//span[@class='visually-hidden']").text == "Unlike" else False
        if isLiked:
            print("The last post has already been liked.")
        else: 
            latest_like_button.click() 
            print("The last post has been liked.")

def main():
    print("-- STARTING BROWSER --")

    account = LinkedInAccount()
    account.sign_in(LOGIN_URL, EMAIL, PASSWORD)
    account.like_latest_post(PROFILE_ACTIVITY_URL)

    print("-- FINISHED --")
    sleep(3) # Sleeps for 3 seconds...

if __name__ == '__main__':
    main()
