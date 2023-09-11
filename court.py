from selenium import webdriver
from lxml import html
from bs4 import BeautifulSoup as BS
import csv, re

out = open("output.csv","w",newline="")


row = csv.writer(out)
row.writerow(["S. No","Diary No. / Case No.[STATUS]","Petitioner Vs. Respondent","Listing Date / Court No."])

path = 'C:/Users/PAWAN/Downloads/geckodriver-v0.28.0-win64/geckodriver.exe'
driver = webdriver.Firefox(executable_path=path)
url = "http://delhihighcourt.nic.in/case.asp" 
driver.get(url)
driver.find_element_by_name("cno").send_keys("1")
year = '2021'
change_year = f"$('select').val('{year}').change()"
driver.execute_script(change_year)
given_value = re.search(' Enter digit (.*?) in text field',driver.page_source).group(1)
driver.find_element_by_id('inputdigit').send_keys(given_value)
tree = html.fromstring(driver.page_source)
driver.find_element_by_tag_name("button").click()
soup = BS(driver.page_source,"html.parser")

ul = soup.find("ul","clearfix grid")

for li in ul.find_all("li"):
    span = li.find_all("span")
    row.writerow([span[0].text.strip(),span[1].text.strip(),span[2].text.strip(),span[3].text.strip()])
# driver.close()
print("-------done-----")
