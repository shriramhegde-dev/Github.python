#stores user_name,worked_hours,access_code
user_name="Googler"
access_code=1234
worked_hours=2
if worked_hours>8:
    print("over_payment")
    print("welcome "+user_name)
    print("Enjoy your free lunch too..")
elif worked_hours>5:
    print("enjoy free lunch")
else:
    print("keep working,free lunch is coming")

