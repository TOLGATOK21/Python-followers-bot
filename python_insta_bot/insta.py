from selenium import webdriver
import time
import kullanici_bilgileri as kb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Browser:
    def __init__(self,link):
        self.link = link
        self.browser = webdriver.Chrome()
        Browser.goInsta(self)
    
    def goInsta(self):
        self.browser.get(self.link)
        
        time.sleep(3)
        Browser.login(self)
        Browser.getFollowers(self)
       

    def getFollowers(self):
        #WE RECEIVE FOLLOWER NAMES FROM THE WEBSITE VIA XPATH
        self.browser.get(self.link+"/"+kb.userName+"/followers/")
        time.sleep(3)
        
        
        Browser.scrollDown(self)
        
        followers= self.browser.find_elements(By.CSS_SELECTOR, value='._ap3a._aaco._aacw._aacx._aad7._aade')
        #In here ı count that followers and after that ı will write this user names in text file.
        counter=0
        with open("followers.txt","w") as file:
         file.write("YOUR CURRENT FOLLOWERS")
         for i in followers:
            counter+=1
            file.write(str(counter)+"-->"+i.text+"\n")
         file.write("YOUR TOTAL FOLLLOWERS : " + str(counter))
            
            

    
    def scrollDown(self):
        jsKomut="""
        sayfa = document.querySelector("._aano");
        sayfa.scrollTo(0,sayfa.scrollHeight);
        var sayfaSonu = sayfa.scrollHeight;
        return sayfaSonu;


        """
        sayfaSonu = self.browser.execute_script(jsKomut)
        while True:
            son =sayfaSonu
            time.sleep(1)
            sayfaSonu = self.browser.execute_script(jsKomut)
            if son == sayfaSonu:
                break



    def login(self):
        #login process
        username = self.browser.find_element(by="name" , value="username")
        password = self.browser.find_element(by="name" , value="password")

        username.send_keys(kb.userName)
        password.send_keys(kb.password)

        time.sleep(2)
        login_button = self.browser.find_element(By.XPATH , value='//*[@id="loginForm"]/div/div[3]')

        login_button.click()
        time.sleep(8) #here timesleep is 8 second because we should for login process. 

        self.browser.get(self.link+"/"+kb.userName)
        time.sleep(4)