import json 

from datetime import datetime, timedelta 

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
        record={"Study-Date":study_date,"Course":course,"Unit-name":unit,"Revision -1":revision_1,"Revision-2":revision_2,"Revision-3": revision_3}
        return record 
    except ValueError:
        print("Invalid Date")
        exit()
    
records=[]
try:
    with open("study_records.json","r")as file:
        records=json.load(file)
except FileNotFoundError:
    records=[]
n=1
while(n>0):
    records.append(create_record())
    n=n-1
with open("study_records.json","w") as file:
    json.dump(records,file,indent=4, default=str)
print (records)