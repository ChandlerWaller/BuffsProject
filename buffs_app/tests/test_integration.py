from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from django.urls import reverse
from django.contrib.auth.models import User
from buffs_app.models import *

from selenium.webdriver.chrome.service import Service as Chrome
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class E2ETestCase(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.get("http://127.0.0.1:8000/")
        print(cls.selenium.title)
        assert 'Shift' in cls.selenium.title

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_user_registration_flow(self):
        # Navigate to the registration page
        self.selenium.get(self.live_server_url + '/register')

        # Enter registration details
        self.selenium.find_element("name", "Username").send_keys('testuser')
        self.selenium.find_element("name", "Password").send_keys('testpass123')
        self.selenium.find_element("name", "Submit").click()

        # Assert successful registration page
        current_url = self.selenium.current_url
        self.assertEqual(current_url, self.live_server_url + "/")

    def test_user_login(self):
        self.selenium.get(self.live_server_url + '/login/')
        # Simulate user login
        self.selenium.find_element("name", "username").send_keys('Presley')
        self.selenium.find_element("name", "password").send_keys('PPHead')
        self.selenium.find_element("name", "Submit").click()

        # Assert successful login page
        current_url = self.selenium.current_url
        self.assertEqual(current_url, self.live_server_url + "/login/")

    def test_shift(self):
        self.selenium.get(self.live_server_url + '/shift/2')
        current_url = self.selenium.current_url
        self.assertEqual(current_url, self.live_server_url + "/shift/2")

    def test_navbar(self):
        self.selenium.get(self.live_server_url)
        self.selenium.find_element("class name", "nav-link").click()
        current_url = self.selenium.current_url
        self.assertEqual(current_url, self.live_server_url + "/")