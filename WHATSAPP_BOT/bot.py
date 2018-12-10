try : 
  from selenium import webdriver
except : 
  print('Need selenium to run try : \n\tpip install selenium')
import os
def main():
	driver = webdriver.Chrome()
	driver.get('https://web.whatsapp.com/')
	name = input('Enter the name of user or group: ')
	msg = input('Enter your message: ')
	count = int(input('Enter the count: '))
	input('Enter any key after scanning QR code')
	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()

	msg_box = driver.find_element_by_class_name('_2bXVy')
		
	for i in range(count):
		msg_box.send_keys(msg)
		button = driver.find_element_by_class_name('_2lkdt')
		button.click() 
	print('Bombing Complete!!')
if __name__ == "__main__" : 
  main()
