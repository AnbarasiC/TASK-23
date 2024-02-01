"""Using Python Selenium Automation and Action Chains visit the URL
https://jqueryui.com/droppable/ and do a Drag and Drop operation of the
White Rectangular Box into the Yellow Rectangular Box?"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


class DragAndDrop:
    # Set up the driver
    def setup_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    # Open the URL
    def open_url(self):
        self.driver.get("https://jqueryui.com/droppable/")
        self.driver.maximize_window()

    def perform_action(self):
        # Switching to iframe
        self.driver.switch_to.frame(0)

        # Finding the draggable and droppable elements
        source_ele = self.driver.find_element(By.ID, "draggable")
        target_ele = self.driver.find_element(By.ID, "droppable")

        # Performing the drag and drop operation
        act = ActionChains(self.driver)
        act.drag_and_drop(source_ele, target_ele).perform()
        time.sleep(5)
        print("Drag and drop operation executed Successfully!..")

    # Close the browser window
    def quit_driver(self):
        self.driver.quit()


drp = DragAndDrop()
drp.setup_driver()
drp.open_url()
drp.perform_action()
drp.quit_driver()
