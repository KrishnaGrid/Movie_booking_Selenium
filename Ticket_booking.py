from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
a = input("Enter number of seats you want to book:-")
website = "https://in.bookmyshow.com/hyderabad/movies/kabzaa/ET00315054"
path = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(path)
# WebDriver driver = new ChromeDriver()
driver.get(website)

ok_field = driver.find_element_by_xpath(
    '/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/div[2]/div/button/div')
ok_field.click();
ok_field = driver.find_element_by_xpath(
    '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/ul/li[3]/section[2]/div')
ok_field.click();
# ok_field = driver.find_element_by_xpath(
#     )
element = driver.find_element_by_xpath('/html/body/div[5]/section[2]/div[3]/div/ul/li[4]/div[2]/div[2]/div[3]/a')
element.click();
sleep(5)
notifiaction_cancel = driver.find_element_by_xpath('/html/body/div[20]/div[2]/div[3]/button[1]')
notifiaction_cancel.click()
sleep(5)
agree_button = driver.find_element_by_xpath('/html/body/div[18]/strong/div[4]/div[2]/div[2]/div/div[3]')
agree_button.click();
sleep(5)
button = driver.find_element_by_xpath('/html/body/div[18]/strong/div[6]/div[2]/div[2]/ul/li['+a+']')
button.click();
sleep(2)
select_button = driver.find_element_by_xpath('/html/body/div[18]/strong/div[6]/div[2]/div[4]/div')
select_button.click();
sleep(2)

select_seat = driver.find_element_by_xpath('/html/body/section/div[3]/section[1]/div/div[2]/div[3]/div/div[1]/table/tbody/tr[15]/td[2]/div[9]')
select_seat.click()
sleep(3)
ActionChains(driver).move_to_element(select_seat).click().perform()
sleep(3)
#Payment Part
payment = driver.find_element_by_xpath('/html/body/section/div[3]/section[1]/div/div[6]/a[1]')
payment.click()
sleep(4)

proced_to_pay = driver.find_element_by_xpath('/html/body/section/div[3]/section[2]/div[3]/div/div[5]/div')
proced_to_pay.click()
sleep(3)

email_field = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/div[1]/div[3]/div[2]/div/div[1]/div[1]/input')
email_field.send_keys('krishna.sahk778@gmail.com')
sleep(2)
phone_field = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/div[1]/div[3]/div[2]/div/div[1]/div[2]/input')
phone_field.send_keys('9170379850')












# actions = ActionChains(driver)
# actions.click(element).perform()
# ok_field = driver.find_element_by_xpath('')
#
#
#
# # ok_field.click();
#
# sleep(20)

# /html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/div[2]/div/button/div

# /html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/ul/li[3]/section[2]/div

# /html/body/div[5]/section[2]/div[3]

#/html/body/div[5]/section[2]/div[3]/div/ul/li[2]/div[2]/div[2]/div[2]/a/div

# /html/body/div[18]/strong/div[4]/div[2]/div[2]/div/div[3]


# last row selecting
#/html/body/section/div[3]/section[1]/div/div[2]/div[3]/div/div[1]/table/tbody/tr[4]/td[+b+]
#start seat
#/html/body/section/div[3]/section[1]/div/div[2]/div[3]/div/div[1]/table/tbody/tr[4]/td[2]/div[2]

#/html/body/section/div[3]/section[1]/div/div[2]/div[3]/div/div[1]/table/tbody/tr[4]/td[2]
# /html/body/section/div[3]/section[1]/div/div[2]/div[3]/div/div[1]/table/tbody/tr[2]/td[2]/div[1]

# Email Input Field
# /html/body/div[5]/div/div/div[3]/div[1]/div[3]/div[2]/div/div[1]/div[1]/input

#phone Input Field
#/html/body/div[5]/div/div/div[3]/div[1]/div[3]/div[2]/div/div[1]/div[2]/input


#/html/body/section/div[3]/section[1]/div/div[2]/div[3]/div/div[1]/table/tbody/tr[13]/td[2]/div[13]/a
# /html/body/section/div[3]/section[1]/div/div[2]/div[3]/div/div[1]/table/tbody/tr[10]/td[2]/div[11]/a