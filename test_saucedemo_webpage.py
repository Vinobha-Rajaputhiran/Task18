"""
test_saucedemo_webpage.py
"""

from saucedemo_webpage import Saucedemo
import pytest

url = 'https://www.saucedemo.com/'
#Postive UserData
#sauce = Saucedemo(url, 'standard_user', 'secret_sauce')

#Negative UserData
sauce = Saucedemo (url,'locked_out_user', 'secret_sauce')

#Test case to lauch the webpage
def test_start_automation():
   assert sauce.start_automation() == True

#Test case for webpage login
def test_login():
   assert sauce.webpage_login() == True

#Test Case to verify valid title
def test_positive_title():
   assert sauce.fetch_webpage_title() == 'Swag Labs'

#Test Case to verify invalid title
def test_negative_title():
   assert sauce.fetch_webpage_title() == 'Not a Lab'

#Test Case to verify valid URL
def test_positive_fetch_weburl():
   assert sauce.fetch_weburl() == 'https://www.saucedemo.com/inventory.html'

#Test Case to verify valid URL
def test_negative_fetch_weburl():
   assert sauce.fetch_weburl() == 'https://www.notasauce.com'

#Test Case to fetech details
def test_fetch_details():
   assert sauce.fetch_details() == True

#Test case to logout
def test_logout():
   assert sauce.webpage_logout() == True

#Test Case to close the browser
def test_shutdown():
   assert sauce.shutdown_automation() == None
