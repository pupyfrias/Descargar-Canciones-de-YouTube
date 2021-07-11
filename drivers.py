from selenium import webdriver
import os,sys

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from subprocess import CREATE_NO_WINDOW

os.system("cls")



def driver():
    try:
        service = Service('./driver/chromedriver')
        service.creationflags = CREATE_NO_WINDOW
        options = webdriver.ChromeOptions()
        user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
        options.add_argument("--start-maximized")
        options.add_argument(f'--user-agent={user_agent}')
        driver = webdriver.Chrome(chrome_options = options, service= './driver/chromedriver.exe' and service)
        
    except:
        try:
            service = Service('./driver/geckodriver')
            service.creationflags = CREATE_NO_WINDOW
            options = webdriver.FirefoxOptions()
            user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
            options.add_argument("--start-maximized")
            options.add_argument(f'--user-agent={user_agent}')
            driver = webdriver.Firefox(options= options, service= './driver/geckodriver.exe'and service)
        except:
            try:
                service = Service('./driver/MicrosoftWebDriver')
                service.creationflags = CREATE_NO_WINDOW
                options = webdriver.EdgeOptions()
                user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
                options.add_argument("--start-maximized")
                options.add_argument(f'--user-agent={user_agent}')
                driver = webdriver.Edge(options= options, service= './driver/MicrosoftWebDriver.exe'and service)

            except:
                exit()

    return driver

