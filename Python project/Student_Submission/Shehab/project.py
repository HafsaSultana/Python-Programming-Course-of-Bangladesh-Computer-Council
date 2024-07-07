import csv

with open ('result.csv','w',newline='') as final:
    write=csv.writer(final)
     
    write.writerow(['Name','Mark','Result'])

with open ('student.csv','r') as file:
    read=csv.reader(file)
    next(read)
    result=''
    for row in read:
        r=row[1]
        value=int(r)
        if 100>=value>=80:
           result='A+'
        elif 79>=value>=70:
           result='A'
        elif 69>=value>=60:
           result='A-'  
        elif 59>=value>=50:
           result='B'        
        elif 49>=value>=40:
           result='C'   
        elif 39>=value>=33:
           result='D'     
        else:
           result='F'
        with open ('result.csv','a',newline='') as final:
             write=csv.writer(final)
     
             write.writerow([row[0],r,result])
             
            
  