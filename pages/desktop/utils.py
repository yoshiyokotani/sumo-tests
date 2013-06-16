#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import selenium.common.exceptions as Exceptions

from pages.page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from unittestzero import Assert


class Utils(Page):

    header_element_locator = (By.XPATH, "//a[@id='tabzilla']")
    footer_element_locator = (By.XPATH, "//footer//li/a[text()='Source Code']")

    def __init__(self, testsetup):
        self.selenium = testsetup.selenium
        self.timeout = testsetup.timeout

    def find_element_and_wait(self, parent=None, by=By.ID, value=None): 
        if parent is None:
            parent = self.selenium        
        try:
            element = WebDriverWait(self.selenium, self.timeout). \
                                    until(lambda s: parent.find_element(by, value))        
        except Exceptions.WebDriverException:
            print "find_element_and_wait: failed to find the target element"
            element = None 
        return element

    def find_element_wait_assert_click(self, parent=None, by=By.ID, value=None):
        element = self.find_element_and_wait(parent, by, value)
        Assert.not_none(element)
        element.click()
        return element

    def find_elements_and_wait(self, parent=None, by=By.ID, value=None):
        if parent is None:
            parent = self.selenium
        try:
            elements = WebDriverWait(self.selenium, self.timeout). \
                                     until(lambda s: parent.find_elements(by, value))
        except Exceptions.TimeoutException:
            print "find_elements_and_wait: failed to find the target element"
            elements = None
        return elements

    def find_elements_wait_assert_click(self, parent=None, by=By.ID, value=None):
        elements = self.find_elements_and_wait(parent, by, value)
        num_elements = len(elements)
        for index in range(num_elements):
            element = elements[index]
            #go to one of the links
            element.click()
            #come back
            self.selenium.back()
            #run find_elements again
            elements = self.find_elements_and_wait(parent, by, value)
        return elements

    def match_urls(self, url):
        current_addr = self.selenium.current_url
        if current_addr == url:
            return True
        else:
            return False

    def scroll_page(self, direction='down'):
        bRet = False
        if direction == "up":
            #find one of the elements located in the header
            element = self.find_element_and_wait(None, *self.header_element_locator)
        elif direction == "down":
            #find one of the elements located in the footer
            element = self.find_element_and_wait(None, *self.footer_element_locator)
        else:
            element = None
        if element is not None:
            element.location_once_scrolled_into_view
            bRet = True
        return bRet
