from requestium import Session, Keys

# If you want requestium to type your username in the browser for you,
# write it in here:
reddit_user_name = ''

s = Session('./chromedriver', browser='chrome', default_timeout=15)
s.driver.get('http://reddit.com')
s.driver.find_element_by_xpath(
    "//a[@href='https://www.reddit.com/login']").click()

print('Waiting for elements to load...')
s.driver.ensure_element_by_class_name(
    "desktop-onboarding-sign-up__form-toggler", state='visible').click()

if reddit_user_name:
    s.driver.ensure_element_by_id('user_login').send_keys(reddit_user_name)
    s.driver.ensure_element_by_id('passwd_login').send_keys(Keys.BACKSPACE)
print('Please log-in in the chrome browser')

s.driver.ensure_element_by_class_name(
    "desktop-onboarding__title", timeout=60, state='invisible')
print('Thanks!')

if not reddit_user_name:
    reddit_user_name = s.driver.xpath(
        "//span[@class='user']//text()").extract_first()

if reddit_user_name:
    s.transfer_driver_cookies_to_session()
    response = s.get(
        "https://www.reddit.com/user/{}/".format(reddit_user_name))
    cmnt_karma = response.xpath(
        "//span[@class='karma comment-karma']//text()").extract_first()
    reddit_golds_given = response.re_first(r"(\d+) gildings given out")
    print("Comment karma: {}".format(cmnt_karma))
    print("Reddit golds given: {}".format(reddit_golds_given))
else:
    print("Couldn't get user name")
