from datetime import datetime, timedelta 
def get_date():
    date_input=input("Enter study date(DD-MM-YYYY):")
    study_date=datetime.strptime
(date_input,"%d-%m-%Y").date()
    return study_date
def revisiondates(study_date):
  next_day=study_date+timedelta (days=1)
  next_week=study_date+timedelta (days=7)
  next_month=study_date+timedelta (days=30)
  return next_day, next_week, next_month
study_date=get_date()
revision_1, revision_2, revision_3=revisiondates(study_date)
course=input ("Enter course:")
unit=input ("Enter unit:")

print("\n")
print("Student Record")
print("_________________")
print("Date:",study_date)
print("Course:", course )
print("Unit:", unit)
print("\n")
print("Revision 1:", revision_1)
print("Revision 2:", revision_2)
print("Revision 3:", revision_3)

