from time import sleep
import threading
g=140

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def get_chrome_driver(url):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    

    
    chrome_options = Options()
    chrome_options.headless=True
    chrome_options.add_argument('--disable-gpu') 
    chrome_options.add_argument("--disable-infobars") 

    chrome_options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    }
    })
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', 'ignore-certificate-errors'])
    
    webdriver = webdriver.Chrome(chrome_options=chrome_options)
    

    webdriver.get(url)
    
    

    return webdriver
    
def pr(i):
    f=open('1.txt','r')
    lines=f.readlines()
    xx=lines[i-1]
    f.close()
    return xx
def a():

    i=1
    url = "https://btcspinner.io/login"
    try:
    	driver = get_chrome_driver(url)
    except:
	    driver = get_chrome_driver(url)

    while True:
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element_by_id("email").send_keys(str(pr(i)))           
        except:
            pass
        try:
            driver.find_element_by_id("password").send_keys("09154831493")
        except:
            pass
        try:
            driver.find_element_by_xpath("//button[@type='submit']").click()

        except:
            pass
        

        try:
            driver.get("https://btcspinner.io/faucet")
            
        except:
            pass
         
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(0.2)
            driver.find_element_by_xpath("//button[@type='submit']").click()
            print(i)
        except:
            pass
            
        sleep(2.5)
        try:
            e=driver.find_element_by_id("navbarDropdown")
            sleep(0.2)
            e.click()
        except:
            pass
        try:
            na=driver.find_elements_by_class_name("dropdown-item")
            sleep(0.2)
            na[5].click()

        except:
            pass
        
        try:       
            driver.get("https://btcspinner.io/login")
        except:
            
            pass

        i+=1
        sleep(1)
        if(i>g):
            i=1
def b():

    i=1+g
    url = "https://btcspinner.io/login"
    try:
    	driver = get_chrome_driver(url)
    except:
	    driver = get_chrome_driver(url)

    while True:
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element_by_id("email").send_keys(str(i) + "@padidehsoft.com")           
        except:
            pass
        try:
            driver.find_element_by_id("password").send_keys("09154831493")
        except:
            pass
        try:
            driver.find_element_by_xpath("//button[@type='submit']").click()

        except:
            pass
        

        try:
            driver.get("https://btcspinner.io/faucet")
            
        except:
            pass
         
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(0.2)
            driver.find_element_by_xpath("//button[@type='submit']").click()
            print(i)
        except:
            pass
            
        sleep(2.5)
        try:
            e=driver.find_element_by_id("navbarDropdown")
            sleep(0.2)
            e.click()
        except:
            pass
        try:
            na=driver.find_elements_by_class_name("dropdown-item")
            sleep(0.2)
            na[5].click()

        except:
            pass
        
        try:       
            driver.get("https://btcspinner.io/login")
        except:
            
            pass

        i+=1
        sleep(1)
        if(i>2*g):
            i=1+g
def c():

    i=1+2*g
    url = "https://btcspinner.io/login"
    try:
    	driver = get_chrome_driver(url)
    except:
	    driver = get_chrome_driver(url)

    while True:
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element_by_id("email").send_keys(str(i) + "@padidehsoft.com")           
        except:
            pass
        try:
            driver.find_element_by_id("password").send_keys("09154831493")
        except:
            pass
        try:
            driver.find_element_by_xpath("//button[@type='submit']").click()

        except:
            pass
        

        try:
            driver.get("https://btcspinner.io/faucet")
            
        except:
            pass
         
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(0.2)
            driver.find_element_by_xpath("//button[@type='submit']").click()
            print(i)
        except:
            pass
            
        sleep(2.5)
        try:
            e=driver.find_element_by_id("navbarDropdown")
            sleep(0.2)
            e.click()
        except:
            pass
        try:
            na=driver.find_elements_by_class_name("dropdown-item")
            sleep(0.2)
            na[5].click()

        except:
            pass
        
        try:       
            driver.get("https://btcspinner.io/login")
        except:
            
            pass

        i+=1
        sleep(1)
        if(i>3*g):
            i=1+2*g
def d():

    i=1+3*g
    url = "https://btcspinner.io/login"
    try:
    	driver = get_chrome_driver(url)
    except:
	    driver = get_chrome_driver(url)

    while True:
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element_by_id("email").send_keys(str(i) + "@padidehsoft.com")           
        except:
            pass
        try:
            driver.find_element_by_id("password").send_keys("09154831493")
        except:
            pass
        try:
            driver.find_element_by_xpath("//button[@type='submit']").click()

        except:
            pass
        

        try:
            driver.get("https://btcspinner.io/faucet")
            
        except:
            pass
         
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(0.2)
            driver.find_element_by_xpath("//button[@type='submit']").click()
            print(i)
        except:
            pass
            
        sleep(2.5)
        try:
            e=driver.find_element_by_id("navbarDropdown")
            sleep(0.2)
            e.click()
        except:
            pass
        try:
            na=driver.find_elements_by_class_name("dropdown-item")
            sleep(0.2)
            na[5].click()

        except:
            pass
        
        try:       
            driver.get("https://btcspinner.io/login")
        except:
            
            pass

        i+=1
        sleep(1)
        if(i>4*g):
            i=1+3*g
def e():

    i=1+4*g
    url = "https://btcspinner.io/login"
    try:
    	driver = get_chrome_driver(url)
    except:
	    driver = get_chrome_driver(url)

    while True:
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element_by_id("email").send_keys(str(i) + "@padidehsoft.com")           
        except:
            pass
        try:
            driver.find_element_by_id("password").send_keys("09154831493")
        except:
            pass
        try:
            driver.find_element_by_xpath("//button[@type='submit']").click()

        except:
            pass
        

        try:
            driver.get("https://btcspinner.io/faucet")
            
        except:
            pass
         
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(0.2)
            driver.find_element_by_xpath("//button[@type='submit']").click()
            print(i)
        except:
            pass
            
        sleep(2.5)
        try:
            e=driver.find_element_by_id("navbarDropdown")
            sleep(0.2)
            e.click()
        except:
            pass
        try:
            na=driver.find_elements_by_class_name("dropdown-item")
            sleep(0.2)
            na[5].click()

        except:
            pass
        
        try:       
            driver.get("https://btcspinner.io/login")
        except:
            
            pass

        i+=1
        sleep(1)
        if(i>5*g):
            i=1+4*g
def f():

    i=1+5*g
    url = "https://btcspinner.io/login"
    try:
    	driver = get_chrome_driver(url)
    except:
	    driver = get_chrome_driver(url)

    while True:
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element_by_id("email").send_keys(str(i) + "@padidehsoft.com")           
        except:
            pass
        try:
            driver.find_element_by_id("password").send_keys("09154831493")
        except:
            pass
        try:
            driver.find_element_by_xpath("//button[@type='submit']").click()

        except:
            pass
        

        try:
            driver.get("https://btcspinner.io/faucet")
            
        except:
            pass
         
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(0.2)
            driver.find_element_by_xpath("//button[@type='submit']").click()
            print(i)
        except:
            pass
            
        sleep(2.5)
        try:
            e=driver.find_element_by_id("navbarDropdown")
            sleep(0.2)
            e.click()
        except:
            pass
        try:
            na=driver.find_elements_by_class_name("dropdown-item")
            sleep(0.2)
            na[5].click()

        except:
            pass
        
        try:       
            driver.get("https://btcspinner.io/login")
        except:
            
            pass

        i+=1
        sleep(1)
        if(i>6*g):
            i=1+5*g
def h():

    i=1+6*g
    url = "https://btcspinner.io/login"
    try:
    	driver = get_chrome_driver(url)
    except:
	    driver = get_chrome_driver(url)

    while True:
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element_by_id("email").send_keys(str(i) + "@padidehsoft.com")           
        except:
            pass
        try:
            driver.find_element_by_id("password").send_keys("09154831493")
        except:
            pass
        try:
            driver.find_element_by_xpath("//button[@type='submit']").click()

        except:
            pass
        

        try:
            driver.get("https://btcspinner.io/faucet")
            
        except:
            pass
         
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(0.2)
            driver.find_element_by_xpath("//button[@type='submit']").click()
            print(i)
        except:
            pass
            
        sleep(2.5)
        try:
            e=driver.find_element_by_id("navbarDropdown")
            sleep(0.2)
            e.click()
        except:
            pass
        try:
            na=driver.find_elements_by_class_name("dropdown-item")
            sleep(0.2)
            na[5].click()

        except:
            pass
        
        try:       
            driver.get("https://btcspinner.io/login")
        except:
            
            pass

        i+=1
        sleep(1)
        if(i>7*g):
            i=1+6*g
def k():

    i=1+7*g
    url = "https://btcspinner.io/login"
    try:
    	driver = get_chrome_driver(url)
    except:
	    driver = get_chrome_driver(url)

    while True:
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element_by_id("email").send_keys(str(i) + "@padidehsoft.com")           
        except:
            pass
        try:
            driver.find_element_by_id("password").send_keys("09154831493")
        except:
            pass
        try:
            driver.find_element_by_xpath("//button[@type='submit']").click()

        except:
            pass
        

        try:
            driver.get("https://btcspinner.io/faucet")
            
        except:
            pass
         
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(0.2)
            driver.find_element_by_xpath("//button[@type='submit']").click()
            print(i)
        except:
            pass
            
        sleep(2.5)
        try:
            e=driver.find_element_by_id("navbarDropdown")
            sleep(0.2)
            e.click()
        except:
            pass
        try:
            na=driver.find_elements_by_class_name("dropdown-item")
            sleep(0.2)
            na[5].click()

        except:
            pass
        
        try:       
            driver.get("https://btcspinner.io/login")
        except:
            
            pass

        i+=1
        sleep(1)
        if(i>8*g):
            i=1+7*g
threading.Thread(target=a).start()
threading.Thread(target=b).start()
threading.Thread(target=c).start()
threading.Thread(target=d).start()
threading.Thread(target=e).start()
threading.Thread(target=f).start()
threading.Thread(target=h).start()
threading.Thread(target=k).start()

