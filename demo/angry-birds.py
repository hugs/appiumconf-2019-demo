from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

#caps = {'automationName': 'arduino', 'app': 'Angry Birds',
#        'newCommandTimeout': 60 * 60}
#driver = webdriver.Remote('http://localhost:4847/wd/hub', caps)

#actions = TouchAction(driver)

global driver
global actions

def connect():
    global actions
    global driver
    caps = {'automationName': 'arduino', 'app': 'Angry Birds',
            'newCommandTimeout': 60 * 60}
    driver = webdriver.Remote('http://localhost:4847/wd/hub', caps)
    actions = TouchAction(driver)


def swipe_right():
    actions.press().perform()
    sleep(.1)
    actions.move_to(x=30,y=0).perform()
    sleep(.1)
    actions.release().perform()
    sleep(.1)
    actions.move_to(x=-30,y=0).perform()


def swipe_left():
    actions.press().perform()
    sleep(.1)
    actions.move_to(x=-30,y=0).perform()
    sleep(.1)
    actions.release().perform()
    sleep(.1)
    actions.move_to(x=30,y=0).perform()


def origin():
    actions.move_to(x=-127,y=-127) \
        .move_to(x=-127,y=-127) \
        .move_to(x=-127,y=-127) \
        .move_to(x=-127,y=-127).perform()
    sleep(.1)


def click():
    actions.press().perform()
    sleep(.1)
    actions.release().perform()
    sleep(.1)


def go(x,y):
    origin()
    actions.move_to(x=x,y=y).perform()
    sleep(.1)



def go_to_bird():
    go(58,85)
    sleep(.5)


def play():
    print("Throw bird...")
    throw_bird()
    sleep(2)
    print("Skip to score...")
    skip_to_score()
    #sleep(5)
    #print("Repeat level!")
    #repeat_level()


def throw_bird():
    go_to_bird()
    actions.press().perform()
    sleep(1)
    for i in range(20):
        actions.move_to(x=-1,y=0).perform()
        sleep(.05)
    for i in range(19):
        actions.move_to(x=0,y=1).perform()
        sleep(.05)
    sleep(1)
    actions.release().perform()
    sleep(1)


def skip_to_score():
    origin()
    actions.move_to(x=100,y=10) \
        .move_to(x=65,y=0) \
        .move_to(x=0,y=100) \
        .move_to(x=0,y=46) \
        .perform()
    sleep(1)
    click()


def repeat_level():
    origin()
    actions.move_to(x=86,y=125).move_to(x=0,y=11).perform()
    sleep(.1)
    click()

if __name__ == "__main__":
    print("Connecting to Appium Server...")
    connect()
    play()
    sleep(2)
    print("Exiting...")
    driver.quit()


# driver.quit()


# Dir: /Users/hugs/Projects/appium/sample-code/python
#URL = 'http://localhost:7774/wd/hub'
#caps = {}
#caps['automationName'] = 'arduino'
#caps['platformName'] = iOS
#caps['app'] = ' '
#e = driver.find_element_by_id("origin")
#TouchAction(driver).tap(e, 104, 255, 1).perform()