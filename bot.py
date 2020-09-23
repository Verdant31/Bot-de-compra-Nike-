from config import keys
from selenium import webdriver
import time
def order(k):
	driver = webdriver.Chrome('./chromedriver')
	
	driver.get(k['product_url'])


	driver.find_element_by_xpath('//*[@id="variacoes"]/div/div[2]/ul/li[2]/label').click()
	driver.find_element_by_xpath('//*[@id="btn-comprar"]').click()
	time.sleep(1)
	driver.get("https://www.nike.com.br/Carrinho")
	time.sleep(1)
	driver.get("https://www.nike.com.br/Checkout")
	driver.find_element_by_xpath('//*[@id="identificacao-guest"]/div/a[1]').click()
	time.sleep(1)
	driver.find_element_by_xpath('//input[@placeholder="Endereço de e-mail"]').send_keys(k["email"])
	driver.find_element_by_xpath('//input[@placeholder="Senha"]').send_keys(k["senha"])
	time.sleep(3)
	driver.find_element_by_xpath('//input[@value="ENTRAR"]').click()
	time.sleep(7)
	driver.find_element_by_xpath('//button[@id="seguir-pagamento"]').click()
	time.sleep(4)
	driver.find_element_by_xpath('//button[@class="button undefined"]').click()
	time.sleep(4)
	
if __name__ == '__main__':
	order(keys)
