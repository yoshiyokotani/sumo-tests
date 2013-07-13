#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from pages.desktop.knowledge_base_article import KnowledgeBaseArticle
import re
import time
from selenium.webdriver.common.by import By
from random import randrange
from selenium.webdriver.common.action_chains import ActionChains
from selenium.selenium import selenium

class ContributorsPage(Base):
    """
    The Firefox Contributors Page contains
    web elements and methods that can be
    performed on them.
    """
    _page_title = 'Knowledge Base Dashboard | Mozilla Support'
    _page_url = '/en-US/contributors'
    _this_week_button_locator = (By.LINK_TEXT, 'This Week')
    _all_time_button_locator = (By.LINK_TEXT, 'All Time')
    _documents_table_busy_locator = (By.CSS_SELECTOR, 'table.documents.busy')
    _top_most_visited_article_locator = \
        (By.CSS_SELECTOR, '#most-visited-table > tr:nth-of-type(2) > td:nth-of-type(1) > a')
    _topic_contributors_locator = (By.CSS_SELECTOR, "ul[class='double'] > li > a")
    _topics_quickstart_guide_locator = (By.CSS_SELECTOR, "div[class='grid_3'] > a")
    _topics_news_and_resources_guide_locator = (By.CSS_SELECTOR, "section[id='doc-content'] > a")
    _forums_contributor_forums_locator = (By.CSS_SELECTOR, "div[class='name'] > a")
    _forum_title_contributor_forums_locator = (By.CSS_SELECTOR, "div[class='title'] > a")
    _post_new_thread_forum_locator = (By.ID, 'new-thread')
    _post_text_forum_locator = (By.ID, 'id_content')
    _post_thread_button_locator = (By.CLASS_NAME, 'btn btn-submit big')
    _post_title_locator = (By.CLASS_NAME, 'nomargin')
    _posts_forum_locator = (By.CLASS_NAME, 'posts')
    _authorname_forum_locator = (By.CLASS_NAME, 'author-name')
    _content_forum_locator = (By.CSS_SELECTOR, "div[class='content'] > p")

    def go_to_contributors_page(self):
        self.open(self._page_url)
        self.is_the_current_page

    def choose_topic_via_contributor_tools(self, topic_name):
        #create a link table from topic_name to href
        topics = self.selenium.find_elements(*self._topic_contributors_locator)
        table_name = []
        table_href = []
        len_abs_href = len(self.base_url)
        for topic in topics:
            table_name.append(topic.get_attribute('text'))
            table_href.append(topic.get_attribute('href'))
        #now get the URL for the given topic
        i = 0
        for name in table_name:
            if name == topic_name:
                url = table_href[i]
                break
            i = i + 1
        #go to the URL
        self.open(url[len_abs_href:len(url)])
        return (url == self.url_current_page)

    def click_topic_quickstart_guide(self, topic_index):
        #find elements for topics
        topics = self.selenium.find_elements(*self._topics_quickstart_guide_locator)
        #choose a topic
        topic = topics[topic_index]
        #get the destination URL
        dest_URL = topic.get_attribute('href')
        #click the topic
        topic.click()
        return (dest_URL == self.url_current_page)

    def get_num_topics_news_and_resources(self):
        return len(self.selenium.find_elements(*self._topics_news_and_resources_guide_locator))

    def click_topic_news_and_resources(self, topic_index):
        #find elements for topics
        topics = self.selenium.find_elements(*self._topics_news_and_resources_guide_locator)
        #choose a topic
        topic = topics[topic_index]
        #get the destination URL
        dest_URL = topic.get_attribute('href')
        #click the topic
        topic.click()
        return (dest_URL == self.url_current_page)

    def get_num_forums(self):
        return len(self.selenium.find_elements(*self._forums_contributor_forums_locator))

    def select_forum_create_newthread_from_contributor_forums(self, forum_index, post_title, post_text):
        #find all the forums in the contributor forums page
        forums = self.selenium.find_elements(*self._forums_contributor_forums_locator)
        #choose a forum
        forum = forums[forum_index]
        #get the destination URL
        dest_URL = topic.get_attribute('href')
        #click the link to the selected forum
        forum.click()
        #check if it has landed on the right page
        if dest_URL != self.url_current_page:
            return False
        else:
            #find the last forum thread in the first page
            threads = self.selenium.find_elements(*self._forum_title_contributor_forums_locator)
            last_thread = threads[len(threads)-2]
            #click it
            last_thread.click()
            #post a new thread
            #1. open a new thread
            self.selenium.find_element(*self._post_new_thread_forum_locator).click()
            #2. write a post comment
            self.selenium.find_element(*self._post_thread_button_locator).send_keys(post_title)
            self.selenium.find_element(*self._post_text_forum_locator).send_keys(post_text)
            #3. click the submit button
            self.selenium.find_element(*self._post_thread_button_locator).click()
            #4. validate the author and the content of the post
            is_present = self.check_post_present(post_title, post_text)
            return is_present

    def check_post_present(self, post_title, post_text):
        is_post_present = False
        #check the post title
        title = self.selenium.find_element(*self._post_title_locator).text
        if title == post_title:
            #get the register user name
            user_name = self.get_user_name('default')
            #search for posts, whose author is user_name
            posts = self.selenium.find_elements(*self._posts_forum_locator)
            for post in posts:
                #find the author name and its content
                author = post.find_element(*self._authorname_forum_locator)
                content = post.find_element(*self._content_forum_locator)
                if author.text == user_name and content.text == post_text:
                    is_post_present = True
                    break
        return is_post_present

#   def select_watch_forum_from_contributor_forums(self, forum_index, post_text):

    def click_top_visited_article_link(self):
        self.selenium.find_element(*self._top_most_visited_article_locator).click()
        return KnowledgeBaseArticle(self.testsetup)

    def click_this_week(self):
        self.selenium.find_element(*self._this_week_button_locator).click()
        self.wait_for_ajax()

    def click_all_time(self):
        self.selenium.find_element(*self._all_time_button_locator).click()
        self.wait_for_ajax()
