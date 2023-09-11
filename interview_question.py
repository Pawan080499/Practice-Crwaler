# import re


# def checkEmail(st):
#     return bool(re.search('\w+@\w+\.\w+',st))

# st = "Arun@gmail.com"
# print(checkEmail(st))

# st = "Arun@gmailcom"
# print(checkEmail(st))
    
# print(re.search('(.*?)@',st).group(1))



# from requests import Session
# from bs4 import BeautifulSoup as bs
# from lxml import html
# s = Session()
# s.headers['User-Agent']="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
# url = "https://en.wikipedia.org/wiki/Visual_Studio_Code"
# r = s.get(url)
# soup = bs(r.text,'html.parser')

# title = soup.find('h1').text
# tree = html.fromstring(r.text)
# history = tree.xpath('//span[@id="History"]/parent::h2/following::p//text()')

# print(title)
# print(history)
# 123-345-6789
# import re
# phone = "klsjf lsfj l 123-345-6789 sdfg "

# print(re.search('[0-9]{3}-[0-9]{3}-[0-9]{4}',phone).group(0))





# url = "https://en.wikipedia.org/wiki/Visual_Studio_Code"
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
# driver.get(url)
# title = driver.find_element(By.XPATH,'//h1//text()')
# print(title)




# def number_generator(n):
#     i=0
#     while i<n:
#         yield i
#         i +=1
# gen = number_generator(5)
# for num in gen:
#     print(num)





# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from lxml import html
# import re
# import csv


# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Firefox(executable_path="C:/Users/PAWAN/Downloads/geckodriver-v0.28.0-win64/geckodriver",options=options)
# out = open("1200cdiscount.csv","w",newline="",encoding="utf-8")
# row = csv.writer(out)



# f = open("desktop_links.txt").read().split("\n")
# for i in f[1200:]:
# 	driver.get(i)
# 	x = driver.page_source.replace("\n","")
# 	tree = html.fromstring(driver.page_source)
# 	# mrp = "".join(tree.xpath("//div[@class='stroken']//text()"))
# 	mrp = "".join(re.findall('fpStriked fpStrikedAfter jsFpStrikedAfter jsStriked jsOverlay hideFromPro">(.*?)<',x)).strip()
# 	# price = re.findall('ion":"NewCondition","price":(.*?),',driver.page_source)
# 	price = ".".join(tree.xpath("//span[@class='fpPrice price jsMainPrice jsProductPrice hideFromPro']//text()"))

# 	name = tree.xpath("normalize-space(//h1[@itemprop='name']//text())")
# 	model = ""
# 	url = i
# 	p_type = tree.xpath("normalize-space(//tr//td[contains(string(),'Catégorie')]//parent::td//following-sibling::td//text())")
	
# 	# s_size = "".join(re.findall(' Affichage</th></tr><tr><td>Type</td><td>(.*?)<',driver.page_source))
# 	s_size = "".join(re.findall('Affichage</th></tr><tr><td>Type</td><td>(.*?)</td',x)) + "".join(re.findall('</tr><tr><td>Taille de la diagonale</td><td>(.*?)</td',driver.page_source))

# 	os = tree.xpath("//tr//td[contains(string(),'Système') and contains(string(),'exploitation')]//parent::td//following-sibling::td//text()")
	
# 	processor_series = tree.xpath("normalize-space(//tr//td[contains(string(),'Processeur|Fabricant') or contains(string(),'CPU')]//parent::td//following-sibling::td//text())")
# 	processor_model = "",
# 	graphics = tree.xpath("normalize-space(//tr//td[contains(string(),'Processeur graphique')]//parent::td//following-sibling::td//text())")
# 	hdd = tree.xpath("normalize-space(//tr//td[contains(string(),'Disque dur') or contains(string(),'Stockage principal')]//parent::td//following-sibling::td//text())")
# 	ram = tree.xpath("normalize-space(//tr//td[contains(string(),'RAM') and(not(contains(string(),'max')))]//parent::td//following-sibling::td//text())") + tree.xpath("normalize-space(//tr//td[contains(string(),'Taille installée') and(not(contains(string(),'max')))]//parent::td//following-sibling::td//text())")


# 	touch = tree.xpath("normalize-space(//h3[contains(string(),'Ecran tactile')]//parent::td//following-sibling::td//a//text())")
# 	resolution = tree.xpath("normalize-space(//th[contains(string(),'Affichage')]//following::tr//td[contains(string(),'Résolution')]//parent::td//following-sibling::td//text())") + "".join(re.findall('</tr><tr><td>Résolution native</td><td>(.*?)</td',driver.page_source))
# 	backlit = "".join(tree.xpath("//tr//td[contains(string(),'Rétroéclairage du clavier')]//parent::td//following-sibling::td//text()"))
# 	warrenty = tree.xpath("normalize-space(//tr//td[contains(string(),'Garantie')]//parent::td//following-sibling::td//text())")
# 	seller = "",
# 	stock = "".join(tree.xpath("//p[@class='fpProductAvailability']//text()")).strip()
# 	block_data = "".join(tree.xpath("//div[@id='descContent']//text()|//ul[@class='listebulletpoint']//text()|//div[@id='fpBulletPointReadMore']//text()"))

# 	row.writerow([mrp,price,name,model,url,p_type,s_size,os,processor_series,processor_model,graphics,hdd,ram,touch,resolution,backlit,warrenty,seller,stock,block_data])
# 	print(i)



# my_list=['p','q']
# n=4
# l=[]
# # output= ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5', 'p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4']

# for i in range(1,n+1):
#     for a in my_list:
#         l.append(a+str(i))
# print(l)





# import re
# input_string='purple to contact alice-b99@google.com, Mondey dishwaasher to contact raju123@gmail.com, Roman'
# output=['alice-b99@google.com,', 'raju123@gmail.com,']  ye aana chahiye output
# result=re.findall("\S+@\S+\.\S+",input_string)
# print(result)


# a1 = ['1','2','3','4','5']
# b = ['1','2','3','7']
# # output = 7
# l=[]
# my_list = list(set(my_list))
# my_second_list = list(set(my_second_list))
# print(my_list,my_second_list)
# 
# 
# for i in (b):
#     if i in a:
#         print ("found " + i)
#         b.remove(i)
# print (b)

# for i in b:
#     if i not in a1:
#         print(i)
    
# output = [a for a in b if a not in a1 ]
# print(output)




# 
# import re
# given_text = "[event] Liverpool vs Real Madrid .WEB .HD .DvdRip 2018 Live"
# cleaned_text = re.sub(r'\s*\.\w+\s*', ' ', given_text)
# cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
# print(cleaned_text)