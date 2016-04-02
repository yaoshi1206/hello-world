fname=str(input("Please input the  filename: " ))
fn= open(fname) 
content=fn.readline()
s=""
print(content)
while content:
    s=s+content
   # print('another line')   
    content=fn.readline()
fn.close()    
print(s)
slen=len(s)
x=''
s2=''
s3=''
for i in range(0,slen):
    s1=s[i]
    s2=chr(ord(s1)+13)
    s3=s3+s2
print(s3)
s4="jiami"+fname
fw=open(s4,'w')
fw.write(s3)
fw.close()

    

        

        
        
            
