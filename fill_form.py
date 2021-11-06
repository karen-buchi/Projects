from selenium import webdriver
import time
driver = webdriver.Chrome("../chromedriver2.exe")
form = driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeqwWseSyRTrTq91FdT75Kt0Tm0bfou81TNZ8HG1HSl9uSNWg/viewform?usp=sf_link")

time.sleep(2)
signin_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span')
signin_button.click()

time.sleep(1)
email = "*****" #fill in your email address in place of the "*"
verify_email = driver.find_element_by_xpath('//*[@id="identifierId"]')
verify_email.send_keys(email)

submit_email = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span')
submit_email.click()

time.sleep(2)
password = "***" #fill in your password for your email  in place of the "*"
enter_pass = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
enter_pass.send_keys(password)

pass_click = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span')
pass_click.click()

time.sleep(4)

firstname = "***" #fill in your firstname in place of the "*"
first = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
first.send_keys(firstname)

lastname = "***" #fill in your last name in place of the "*"
first = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
first.send_keys(lastname)

age = 23
first = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
first.send_keys(age)

first = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
first.send_keys(email)

click_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
click_button.click()

get_confirmation_div_text = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[3]')
confirm = get_confirmation_div_text.text
if get_confirmation_div_text == "Your response has been recorded.":
    print("Process Successful")
else:
    print("Not successful")
