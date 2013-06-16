#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from pages.desktop.utils import Utils
from selenium.webdriver.common.by import By


class ForContributorsMenu(Base):
    """
        Menu 'For Contributors'
    """
    #global locators
    _loc_contributors_menu_link = (By.XPATH, ".//*[@id='for-contributors']/header/h1")
    _loc_contributors_menu = (By.ID, "for-contributors")
    _loc_contributors_links = (By.CSS_SELECTOR, "a")
    _loc_header = (By.XPATH, "//a[text()='Ask a question']")
    _loc_footer = (By.XPATH, "//a[text()='Source Code']")

    def __init__(self, testsetup):
        self.testsetup = testsetup
        self.selenium = testsetup.selenium

    def open_contributors_menu(self):
        Utils(self.testsetup).find_element_wait_assert_click(None, *self._loc_contributors_menu_link)
        return

    def is_contributors_menu_displayed(self):
        utils = Utils(self.testsetup)
        #find the menu element
        menu_element = utils.find_element_and_wait(None, *self._loc_contributors_menu)
        #find one of the items belonging to the menu
        item_element = utils.find_element_and_wait(menu_element, *self._loc_contributors_links)
        return item_element.is_displayed()

    def get_links_in_menu(self):
        utils = Utils(self.testsetup)
        #find the menu element
        menu_element = utils.find_element_and_wait(None, *self._loc_contributors_menu)
        #find all the links within the menu
        return utils.find_elements_and_wait(menu_element, *self._loc_contributors_links)

    def click_and_check_url(self, link):
        #check the URL of the Link
        url_destination = link.get_attribute("href")
        #click the Link
        link.click()
        #wait for a specific time duration
        self.selenium.implicitly_wait(10)
        #get the URL of the current Page
        url_actual = self.selenium.current_url
        #compare both URLs
        if url_destination is None or url_destination == url_actual:
            return True
        else:
            return False

    def go_back_page(self):
        self.selenium.back()

    def scroll_page(self, direction="down"):
        Utils(self.testsetup).scroll_page(direction)
