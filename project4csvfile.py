import csv
def write_into_csv(student_info):
    with open('student_informations.csv','a',newline='') as csv_file:
        
        writer=csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Section","Email_id","Contact_number","Branch"])
        writer.writerow(student_info)




condition=True
while (condition):
    info=input("enter information of student in following format ( name  age  section  email_id  contact_number  branch)")
    onfo=info.split()
    print("entered information is :")
    print(onfo)
    a=input("enter yes if the information is correct else enter no")
    if a=="yes":
        write_into_csv(onfo)
        s=input("enter yes for another student or no for break")
        if s=="yes":
            condition=True
        elif s=="no":
            condition=False
    else:
        print("please re-enter the information")
