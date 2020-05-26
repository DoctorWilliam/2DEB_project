f = open("input.txt","r")

f_out= open("output.txt","W") #Apne fila vi skal telle vokaler med lesetilgang

file_content = f.read() #Lagre innhold i fila til file_content som en string

count = 0

for i in file_content:
    if i =='a':
       count = count + 1
       
print(count)

f_out.write("A or a: ")
f_out.write(str(count))

f.close() #Alltid lukk fila etter bruk
f_out.close()