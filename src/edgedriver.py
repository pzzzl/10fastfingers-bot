from config import *
from selenium import webdriver

class Edge:
    def __init__(self):
        self.driver = webdriver.Edge(executable_path=MSEDGEDRIVER_PATH)
        self.driver.implicitly_wait(60)
    def start(self):
        self.driver.get(URL)
        assert "10FastFingers.com" in self.driver.title
        return self.driver
