#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import selenium.common.exceptions as Exceptions

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from unittestzero import Assert

class Utils():

    def __init__(self, testsetup):
        self.selenium = testsetup.selenium
        self.timeout = testsetup.timeout

    @property
    def find_element_and_wait(self,locator,parent=None):
     
        if parent is None:
            parent = self.selenium
        
        try:
            element = WebDriverWait(self.selenium,self.timeout). \
                                    until(lambda s: parent.find_element(*locator))        
        except Exceptions.TimeoutException:
            print "find_element_and_wait: failed to find the target element"
            element = None 
    
        return element

    @property
    def find_element_wait_assert_click(self,locator,parent=None):

        element = None
        #element = self.find_element_and_wait(locator,parent)
        #Assert.none(element)
        #element.click()
        
        return element       
        
    @property
    def find_elements_and_wait(self,locator,parent=None):
        
        if parent is None:
            parent = self.selenium
        
        try:
            elements = WebDriverWait(self.selenium,self.timeout). \
                                     until(lambda s: parent.find_elements(*locator))
        except Exceptions.TimeoutException:
            print "find_elements_and_wait: failed to find the target element"
            elements = None
                
        return elements
    
    @property
    def find_elements_wait_asssert_click(self,locator,parent=None):
    
        elements = self.find_elements_and_wait(locator,parent)
        num_elements = len(elements)
        for i in range(num_elements):
            element = elements[i]
            #go to one of the links
            element.click()
            #come back
            self.go_back_page()
            #run find_elements again
            #elements = self.find_elements_and_wait(locator,parent)
 
    
    def match_urls(self, url1):
        
        current_addr = self.selenium.current_url
        if current_addr == url1:
            return True
        else:
            return False
        
    def go_back_page(self):
        
        self.selenium.back()