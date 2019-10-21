import csv
import xlwt 
from xlwt import Workbook 


usn=int(input("Enter your usn: "))
name=input("Enter your name:  ")
age=int(input("Enter the age: "))



# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 

sheet1.write(1,0,'USN')
sheet1.write(2,0,'Name')
sheet1.write(3,0,'Age')
sheet1.write(0,1,usn)
sheet1.write(0,2,name)
sheet1.write(0,3,age)

wb.save('xlwt userInfo.xls')