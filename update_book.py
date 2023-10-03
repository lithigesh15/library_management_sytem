import mysql.connector as md
from sys import stderr
from datetime import date

db=md.connect(host='localhost',user="root",passwd='root',database='lib')
cur=db.cursor()
cur.execute("select min(id),max(id) from books2 where id>1000")

stderr.write("--------------------------------Update Books---------------------------------\n")
my_range=cur.fetchall();my_range=my_range[0]
cur.execute(f"select copies from books2 where id={my_range[1]}")
copies_max=cur.fetchall()
my_range=[my_range[0],my_range[1]+copies_max[0][0]]
print("U can search & update books btw the given range where upper limit is exclusive - i.e upper limit book doesn't exist.")
print(my_range)
print('\n')

while True:
    b_id=int(input("Enter id to search : "))
    cur.execute("select id,copies from books2");id_copies_list=cur.fetchall()
    id_copies_list.remove((1000,1))
    id_list=[]
    
    for a in id_copies_list:
        id_list.append(a[0])

    cur.execute('select max(sno) from books2');sno=cur.fetchall();sno=sno[0][0]+1
    Date=date.today()

    if b_id in id_list:
        cur.execute(f"select id,name,author,genre,copies from books2 where id={b_id}")
        sch_data=cur.fetchall()
        print(sch_data)

        n_b=input("Enter book name : ")
        n_a=input("Enter author name : ")
        n_genre=input("Enter new genre : ")
        final_data=(sno,b_id,n_b,n_a,n_genre,1,str(Date))
            
        if sch_data[0][-1]==1:
            stderr.write("\nblock - 1 IF running now \n")
            sch_data=list(sch_data[0]);sch_data[0]=b_id
            update_query="id={},name='{}',author='{}',genre='{}',copies={},date_='{}'".format(final_data[1],final_data[2],final_data[3],final_data[4],final_data[5],final_data[6])
            query="update books2 set "+update_query+f" where id={b_id}"
            cur.execute(query)
            db.commit()
            print("Update Succesful !!!")
            print("\n")
                
        else:
            stderr.write("\nblock -1 ELSE running now\n")
            sch_data=list(sch_data[0]);sch_data[0]=b_id;sch_data[-1]=1
            print(sch_data)
            cur.execute(f"update books2 set copies=copies-1,id=id+1 where id={b_id}")
            cur.execute(f"insert into books2 values {final_data}")
            db.commit()
            print("Successfuly Added !!! :)")
            print(f"Added Data : {final_data}")
            print("\n")
            
    elif b_id in range(my_range[0],my_range[1]):
        stderr.write("\nELIF block running now\n")
        my_id=0
        for a in id_copies_list:
            if b_id in range(a[0],a[0]+a[1]+1):
                my_id=a[0]
        print(my_id)
        cur.execute(f"select id,name,author,genre,copies from books2 where id={my_id}")
        sch_data=cur.fetchall();sch_data=list(sch_data[0]);sch_data[0]=b_id;sch_data[-1]=1
        print(sch_data)

        n_b=input("Enter book name : ")
        n_a=input("Enter author name : ")
        n_genre=input("Enter new genre : ")
        final_data=(sno,b_id,n_b,n_a,n_genre,1,str(Date))

        cur.execute(f"update books2 set copies=copies-1 where id={my_id}")
        cur.execute(f"insert into books2 values {final_data}")
        db.commit()
        print("Successfuly Added !!! :)")
        print(f"Added Data : {final_data}")
        print("\n")
        
    else:
        stderr.write("No Book Found :(\n")
