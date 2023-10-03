import mysql.connector as md
db=md.connect(user="root",host='localhost',passwd='root',database="lib")
cur=db.cursor()

cur.execute("select id,name,author,genre,copies from books2 where id=1001")
data=cur.fetchone()
data=list(data)
id_=1002
l=[]
count=0
b_id=data[0]
for a in range(data[-1]):
    b_id_new=b_id+count
    count+=1
    data[0]=b_id_new;data[-1]=1
    if b_id_new==id_:
        continue
    print(data)

    
    
        
    
