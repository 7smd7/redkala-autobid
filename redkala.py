from selenium import webdriver
import time

driver = webdriver.Firefox()


user="bloblob@gmail.com"
password="bloblob"
# name="bloblob"

# driver.get("http://redkala.com/default/lang/Fa")
# driver.find_element_by_link_text(u"ورود به سيستم").click()

driver.get("http://redkala.com/fwk/user/login/lang/Fa")
driver.find_element_by_id("ctl01_ctl00_ctl00_txtUserName").send_keys(user)
driver.find_element_by_id("ctl01_ctl00_ctl00_txtPassword").click()
driver.find_element_by_id("ctl01_ctl00_ctl00_txtPassword").send_keys(password)
driver.find_element_by_id("ctl01_ctl00_ctl00_captcha_ctl00_txtUserInputValue").click()
captcha=input("write captcha: ")
driver.find_element_by_id("ctl01_ctl00_ctl00_captcha_ctl00_txtUserInputValue").send_keys(captcha)
driver.find_element_by_id("ctl01_ctl00_ctl00_btnUpdate").click()
# time.sleep(2)
# if(driver.current_url != "http://redkala.com/default/lang/Fa"):
#     driver.get("http://redkala.com/default/lang/Fa")
print("go manual on sale page...\n")


while(True):
    input("ready?")
    print("Go!")
    try:
        valid=True
        while(valid):
            timer=driver.find_element_by_xpath("/html/body/form/section/section/section/div[7]/div[3]/div/div/div[6]/div[2]/span[2]").text
            # winner=driver.find_element_by_xpath("/html/body/form/section/section/section/div[7]/div[3]/div/div/div[6]/div[2]/div[3]/span").text
            if (timer == '00:00:00'):
                time.sleep(0.3)
                timer=driver.find_element_by_xpath("/html/body/form/section/section/section/div[7]/div[3]/div/div/div[6]/div[2]/span[2]").text                
                if(int(timer[-2:])==0):
                    driver.find_element_by_xpath("/html/body/form/section/section/section/div[7]/div[3]/div/div/div[6]/div[2]/a").click()
                    print("clicked. What's up?!")
                valid=False

    except Exception as e:
        print("ERROR: "+ str(e))
    
    