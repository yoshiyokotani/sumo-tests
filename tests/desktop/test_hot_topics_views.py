#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from unittestzero import Assert
from pages.desktop.page_provider import PageProvider

from selenium import webdriver

#@pytest.mark.skipif("config.getvalue('base_url')=='https://support-dev.allizom.org'")
#class TestHotTopicViews:
       
#    @property
#    def count_number_of_hot_topics(self, mozwebqa):
#        home_page = PageProvider(mozwebqa).home_page()
#        home_page.sign_in('default')
#        page_title = home_page.click_card_grid(home_page.learn_the_basics_locator)
#        Assert.contains('Learn the Basics: get started ', page_title)        
    
#    @pytest.mark.nondestructive
#    def test_click_