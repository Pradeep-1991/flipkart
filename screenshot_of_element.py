from selenium import webdriver
from PIL import Image
driver = webdriver.Chrome(r"D:\selinium_drivers\chromedriver_win32\chromedriver")
driver.get('https://www.google.co.in')
element = driver.find_element_by_name("q")
location = element.location
size = element.size
driver.save_screenshot("pageImage.png")
x = location['x']
y = location['y']
width = location['x']+size['width']
height = location['y']+size['height']
im = Image.open('pageImage.png')
im = im.crop((int(x), int(y), int(width), int(height)))
im.save('element_image.png')


