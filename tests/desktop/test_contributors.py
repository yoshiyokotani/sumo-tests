#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import pytest
from unittestzero import Assert

from pages.desktop.page_provider import PageProvider
from pages.desktop.contributors_page import ContributorsPage
from random import randrange

class TestContributors:

    def test_quickstart_guide(self, mozwebqa):
        category = 'Quickstart Guide'
        num_topics_quickstart_guide = 4

        #1. go to the home page
        home_page = PageProvider(mozwebqa).home_page(True, 'default')
        #2. click the link to the guide
        contributors_page = ContributorsPage(mozwebqa)
        is_loaded_page = contributors_page.choose_topic_via_contributor_tools(category)
        #3. check if it has landed on the right destination
        Assert.true(is_loaded_page)

        #4. click one of the links in the guide
        topic_index = randrange(num_topics_quickstart_guide)
        is_loaded_page = contributors_page.click_topic_quickstart_guide(topic_index)
        Assert.true(is_loaded_page)

        #5. go one page back
        contributors_page.back()

    def test_contributor_forums(self, mozwebqa):
        #4. click one of the links
        num_topics_quickstart_guide = 4
        topic_index = randrange(num_topics_quickstart_guide)
        contributors_page.click_topic('Quickstart guide', topic_index)
        #5. go one page back
        contributors_page.back()