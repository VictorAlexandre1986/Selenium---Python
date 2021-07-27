from selenium import webdriver

nav = webdriver.Chrome()

nav.get('https://www.w3schools.com/')

nav.get_screenshot_as_file('C:\\Users\\Victor\\Desktop\\Aprendendo\\Python\\screenshot.png')

nav.quit()


