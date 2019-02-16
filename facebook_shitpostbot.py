from selenium import webdriver
import time
import random 


 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium" 
#change to the adress of where your chrome driver is located 
driver = webdriver.Chrome('/home/yournameh/Desktop/chromedriver') 
# github : housemateguy 
# github rep : https://github.com/housemateguy/facebook_shitpostbot

#votre email et password 
email="type here"
password="type here"
codeofgroup="1788182868119269"

driver.get('https://m.facebook.com/login/?ref=dbl&fl&refid=8')
print ('current url:' + driver.current_url + '')
# login
text_area = driver.find_element_by_id('m_login_email')
text_area.send_keys(str(email))
text_area2 = driver.find_element_by_id('m_login_password')
text_area2.send_keys(str(password))
time.sleep(3)
loginb = driver.find_element_by_id('u_0_5')
loginb.click()
time.sleep(5)
# comment generator (change if you want)
thislist = ["Geeez,", "lol,", "I can't,","you guys,","AHAHAHAHAHAHA,","SHUT UP,","Don't @me,"] 
thislist2 = ["this group", "the people here", "huwite ppl","you guys","the girl reading this","Donald Trump","your mom"] 
thislist3 = ["is", "are", "are","are","is","is","is"] 
thislist4 = ["GAY","just stupid","boring asf","RTARDED","BIG DUMB DUMB","JUST RTARDED","NOT MY PRESIDENT"]
thislist5 = ["LOL BYE","LOL I'm leaving this group","I petty you guys","GTG","LMOAA","I FEEL BAD FOR YOU!","just please get some help"]
driver.get('https://mbasic.facebook.com/groups/' + str(codeofgroup) + '')
print ('current url: ' + driver.current_url + '')
for x in range(50):   
 #posting loop
 time.sleep(2)
 i= random.randint(0, 6)
 j= random.randint(0, 6)
 k= random.randint(0, 6)
 l= random.randint(0, 6)
 text_area3= driver.find_element_by_id('u_0_0')
 text_area3.send_keys(thislist[i]+' '+thislist2[j]+' '+thislist3[j]+' '+thislist4[k]+' '+thislist5[l])
 submit= driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[1]/div[3]/form/table/tbody/tr/td[3]/div/input")
 submit.click()
 time.sleep(5)




time.sleep(3)
driver.close()
driver.quit()
