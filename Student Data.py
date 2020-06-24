# Project 1
# School Administration
 Input :
import csv

def info(Student_Info) :
    
  with open ('Student_Info.csv' , mode = 'a' , newline = '') as csvfile :
   p = csv.writer(csvfile)
       
   if csvfile.tell () == 0 :
   p.writerow (['Name','Age','Mobile_Number','Email_ID'])
   p.writerow (Student_Info)
        
if __name__ == '__main__' :
    count = 1
    
  while True :
     print ("\nEnter the Student_Info " + str (count) + " in format :\n")
     Student_Info = input ("\nName, Age, Mobile_Number, Email_ID :\n").split (",")
     print(f"\nName : {Student_Info[0]} \nAge : {Student_Info[1]} \nMobile_Number : {Student_Info[2]} \nEmail_ID : {Student_Info[3]}\n")
        
     choice_check = input ("\nInfo is correct (yes/no) :\n")
       if choice_check == 'yes':
        info (Student_Info)
            
     choice_check = input ("\Another student Info (yes/no) ?\n")
        if choice_check == 'no':
             break
          else:
             count += 1
Output : 
Enter the Student_Info 1 in format :


Name, Age, Mobile_Number, Email_ID :
Alex, 12, 1234567890,Alex@gmail.com

Name : Alex 
Age :  12 
Mobile_Number :  1234567890 
Email_ID : Alex@gmail.com


Info is correct (yes/no) :
yes
\Another student Info (yes/no) ?
yes

Enter the Student_Info 2 in format :


Name, Age, Mobile_Number, Email_ID :
Lucky, 15, 9876543210, Lucky15@gmail.com

Name : Lucky 
Age :  15 
Mobile_Number :  9876543210 
Email_ID :  Lucky15@gmail.com


Info is correct (yes/no) :
yes
\Another student Info (yes/no) ?
yes

Enter the Student_Info 3 in format :


Name, Age, Mobile_Number, Email_ID :
cyrus, 19, 6541239870, cyrus18@gmail.com

Name : cyrus 
Age :  19 
Mobile_Number :  6541239870 
Email_ID :  cyrus18@gmail.com


Info is correct (yes/no) :
yes
\Another student Info (yes/no) ?
no
                
                
