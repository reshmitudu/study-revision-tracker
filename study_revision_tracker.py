import json 
from datetime import datetime, timedelta, date

def revisiondates(study_date):
     next_day=study_date+timedelta (days=1)
     next_week=study_date+timedelta (days=7)
     next_month=study_date+timedelta (days=30)
     return next_day, next_week, next_month
def create_record():
     try:
         study_date=input("Enter study date in DD-MM-YYYY:")
         study_date=datetime.strptime(study_date,"%d-%m-%Y").date()
         course=input ("Enter course:")
         unit =input("Enter unit:")
         revision_1,revision_2,revision_3=revisiondates(study_date)
         record={"Study-Date":study_date,"Course":course,"Unit-name":unit,"Revision-1":revision_1,"Revision-2":revision_2,"Revision-3":revision_3}
         return record 
     except ValueError:
         print("Invalid Date")
         exit()
def checkRevision(records):
     due_today=[]
     today=date.today() 

     for record in records:
         rev_1=date.fromisoformat(record["Revision-1"])
         rev_2=date.fromisoformat(record["Revision-2"])
         rev_3=date.fromisoformat(record["Revision-3"])
         if(rev_1==today):
             due_today.append("Revision 1:"+record["Course"]+" - "+record["Unit-name"])
         if(rev_2==today):
             due_today.append("Revision 2:"+record["Course"]+" - "+record["Unit-name"])
         if(rev_3==today):
             due_today.append("Revision 3:"+record["Course"]+" - "+record["Unit-name"])
     print("Revisions Due Today")
     for item in due_today:
         print(item)
     print("\nNo of revisions due today:",len(due_today))        
def menu():
     print("\n=====STUDY REVISION TRACKER=====")
     print("\n1. Add new study record")
     print("\n2. Check revisions due today")
     print("\n3. Exit")

     choice=int(input("\nEnter your choice:"))

     return choice

choice=menu()
print ("You selected:",choice)
match choice:
     case 1:
         try:
             with open("study_records.json","r")as file:
                 records=json.load(file)
         except FileNotFoundError:
             records=[]
         checkRevision(records)
     case 2:
         
         n=1
         while(n>0):
             records.append(create_record())
             n=n-1
         with open("study_records.json","w") as file:
             json.dump(records,file,indent=4, default=str)
     case 3:
         print("Program exits with code 0")
         exit(0)
     case _:
         print ("You entered wrong choice ")
         