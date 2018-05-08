#coding = utf-8
from selenium import webdriver

class Page(object):

    def __init__(self,driver,base_url):
        self.driver = driver
        self.base_url = base_url

    def base_find_element(self,*loc):
        return self.driver.find_element(*loc)

    def base_get_url(self,url):
        return self.driver.get(url)

    def base_input_text(self,loc,text):
        self.base_find_element(*loc).send_keys(text)

    def base_claer(self,loc):
        self.base_find_element(*loc).clear()

    def base_submit(self,loc):
        self.base_find_element(*loc).submit()


    def base_click(self,loc):
        self.base_find_element(*loc).click()

    def base_get_title(self):
        return self.driver.title
    def base_get_text(self,loc):
        return self.base_find_element(*loc).text
    def base_quit(self):
        self.driver.quit()


