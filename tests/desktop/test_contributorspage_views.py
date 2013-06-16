#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.desktop.page_provider import PageProvider
from pages.desktop.utils import Utils
from selenium.webdriver.common.by import By

from pages.desktop.contributors_page import ContributorsPage
from pages.desktop.for_contributors_menu import ForContributorsMenu
from selenium import webdriver
from unittestzero import Assert


class TestContributorsPageViews:

    @pytest.mark.nondestructive
    def test_first_level_view_contributors_menu(self, mozwebqa):

        #go to the home page
        home_page = PageProvider(mozwebqa).home_page()
        home_page.sign_in('default')

        #[H] click the link to open the menu "for contributors"
        menu = ForContributorsMenu(mozwebqa)
        menu.open_contributors_menu()
        #check if the menu has been displayed
        Assert.true(menu.is_contributors_menu_displayed)

        #[H] click and back each one of the links
        result = False
        menu_links = menu.get_links_in_menu()
        num_links = len(menu_links)
        for i in range(num_links):
            menu_link = menu_links[i]
            #[H] go to the link
            result = menu.click_and_check_url(menu_link)
            if result == False:
                break

            #[H] scroll down to the bottom
            result = menu.scroll_page('down')
            if result == False:
                break

            #[H] back to the home page
            menu.go_back_page()

            #[H] open the menu and get the links again
            menu.open_contributors_menu()
            menu_links = menu.get_links_in_menu() 

        #check if the whole process is complete without errors
        Asser.true(result)

        return

    @pytest.mark.nondestructive
    def test_quickstart_guide(self, mozwebqa):

        _loc_quickstart_guide = (By.XPATH, ".//*[@id='for-contributors']/section/ul//li/a[text()='Quickstart Guide']")
        _loc_involvements = (By.XPATH, "//div[@class='row cf pick-a-way']//a")

        #go to the home page
        home_page = PageProvider(mozwebqa).home_page()
        home_page.sign_in('default')

        #open an instance of Utils
        utils = Utils(mozwebqa)

        #[H] click the link to open the menu "for contributors"
        menu = ForContributorsMenu(mozwebqa)
        menu.open_contributors_menu()

        #[H] click the link to the quickstart guide
        utils.find_element_wait_assert_click(None, *_loc_quickstart_guide)

        #[M] find involvement elements (links)
        utils.find_elements_wait_assert_click(None, *_loc_involvements)

    @pytest.mark.nondestructive
    def test_news_and_resources(self, mozwebqa): 

        _loc_news_and_resources = (By.XPATH, ".//*[@id='for-contributors']/section/ul//li/a[text()='News & Resources']")
        _loc_toc = (By.XPATH, "//div[@id='toc']/ul//a")
        _loc_articles = (By.XPATH, "//article//section//ul//li/a")

        #go to the home page
        home_page = PageProvider(mozwebqa).home_page()
        home_page.sign_in('default')

        #open an instance of Utils
        utils = Utils(mozwebqa)

        #[H] click the link to open the menu "for contributors"
        menu = ForContributorsMenu(mozwebqa)
        menu.open_contributors_menu()

        #[H] click the link to the news & resources
        utils.find_element_wait_assert_click(None, *_loc_news_and_resources)

        #[M] find TOC elements (links)
        TOC_links = utils.find_elements_and_wait(None, *_loc_toc)
        Assert.not_none(TOC_links)

        num_TOCs = len(TOC_links)
        for i in range(num_TOCs):
            TOC_link = TOC_links[i]
            #[H] click a link to one of the TOCs  
            TOC_link.click()
            #[H] find all the associated articles
            article_links = utils.find_elements_and_wait(None, *_loc_articles)
            num_article_links = len(article_links)
            for j in range(num_article_links):
                article_link = article_links[j]
                article_link.click()
                #[H] back to the home page
                mozwebqa.selenium.back()
                #[H] find all the associated articles
                article_links = utils.find_elements_and_wait(None, *_loc_articles)