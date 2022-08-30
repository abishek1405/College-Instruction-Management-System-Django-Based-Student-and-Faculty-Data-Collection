class details:
	def __init__(self,Regno,name,Class,section,mark,result):
		self.RegisterNo=Regno
		self.Name=name
		self.Class=Class
		self.Section=section
		self.Mark=mark
		self.Result=result
	def student(self):
		print('RegisterNo :',self.RegisterNo)
		print('Name :',self.Name)
		print('Class :',self.Class)
		print('Section :',self.Section)
		print('Mark :',self.Mark)
		print('Result :',self.Result)
Raju=details(622614114001,'Raju','10th Std','A-Section','400','Pass')
Gopal=details(622614114002,'Gopal','10th Std','B-Section','150','Fail')
Ramya=details(622614114003,'Ramya','10th Std','C-Section','350','Pass')
Ranjith=details(622614114004,'Ranjith','10th Std','B-Section','499','Pass')
Indian=details(622614114005,'Indian','10th Std','A-Section','412','Pass')
Tamilan=details(622614114006,'Tamilan','10th Std','C-Section','298','Pass')
Karthic=details(622614114007,'Karthic','10th Std','A-Section','488','Pass')
Mani=details(622614114008,'Mani','10th Std','A-Section','80','Fail')
Salman=details(622614114009,'Salman','10th Std','C-Section','102','Fail')
Khan=details(622614114010,'Khan','10th Std','C-Section','170','Fail')
F='Y'
while F.upper()=='Y':
	while True:
		a=input("Enter the Student Name For View the Result  :")	
		b=a.title()
		try:
			a=globals()[b]
		except KeyError:
			print("The Name is Not Available On The List, Please Type correct Name Below ")
			continue
		except:
			print("Somthing Went Wrong Please Try Again")
			break
		a.student()
		while True:
			f=input("Press Y to continue and N to exit  :")
			if f.upper()=='Y':
				F=f
			elif f.upper()=='N':
				F=f
				print("Exit")
			else:
				print("You Entered Wrong Key Please Enter Correct Key")
				continue
			break
		break
import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
import re
import csv
import pandas as p

#open the browser
driver=webdriver.Chrome()

url="https://www.gartner.com/en/glossary/all-terms"

#open the url
driver.get(url)

#store the current url
urls=driver.current_url
#html data
obj=requests.get(urls)
#python readable html data
pyobj=BeautifulSoup(obj.content,features="html.parser")
#empty lists
a=[]
b=[]


#user defind function
def content(bc):
	con=1
	#find and append the content of data
	for j in bc.findAll("div",attrs={"class":"row"}):
		if con !=1:
			data=j.text.replace("\n"," ")
			b.append(data)
			break
		con+=1
		
#counts=0
for j in pyobj.findAll("div",attrs={"class":"item-wrapper"}):
	#count=0
	for i in re.finditer(r'<div class="search-item (.*?)">',str(j)):
		ab=i.group(1)
		#find the link text like .net from the web
		st=driver.find_element_by_link_text(ab)
		#click it
		st.click()
		#getting url
		urls=driver.current_url
		obj=requests.get(urls)
		lobj=BeautifulSoup(obj.content,features="html.parser")
		#find and append the word
		st1=lobj.find("div",attrs={"class":"col-md-12 col-sm-12"})
		a.append(st1.text)
		#function call
		content(lobj)
		#browse back
		driver.back()
		#for testing use below code 
		#if count ==5:
		#	break
		#count+=1
	#counts+=1
	#if counts ==5:
	#	break 
	
#frame and save the data's in csv file		
np=p.DataFrame({"WORD":a,"DESCRIPTION":b})	
np.to_csv('Details.csv',index=False,encoding="utf-8")
print("Check The Details.csv File For Details")
	
		