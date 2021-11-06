from selenium import webdriver
import time
import pandas as pd
df = pd.read_csv("../Database.csv", header=0)
a = len(df["Email Address"])
while True:
    counter = 0
    for index in range(a):
        b = df.iloc[index, :]
        email = b["Email Address"]
        firstname = b["First name"]
        lastname = b["Last Name"]
        gender = b["Gender"].lower()
        age = int(b["Age"])
        driver = webdriver.Chrome("../chromedriver2.exe") #this should be leading to the path of the chrome driver on your device
        form = driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf199CGgRmkviKgL6hgWurjI65VKP2mS55eS6QQn2UjQJrEkA/viewform?usp=sf_link")

        time.sleep(4)

        firstname_column = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        firstname_column.send_keys(firstname)

        lastname_column = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        lastname_column.send_keys(lastname)

        age_column = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        age_column.send_keys(age)

        if gender == "female":
            gender_button = driver.find_element_by_xpath('//*[@id="i17"]/div[3]/div')
            gender_button.click()
        elif gender == "male":
            gender_button = driver.find_element_by_xpath('//*[@id="i20"]/div[3]/div')
            gender_button.click()

        email_column = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
        email_column.send_keys(email)

        click_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        click_button.click()

        get_confirmation_div_text = driver.find_element_by_class_name('freebirdFormviewerViewResponseConfirmationMessage')
        confirm = get_confirmation_div_text.text
        if confirm == "Your response has been recorded.":
            print(f"Process Successful, {firstname, lastname}'s information with the email:{email} has been recorded.")

        else:
            print("Not successful")

    break

