a=int(input( "Enter a number:"))
seq=[a]
while a>1:
  if a%2==0 :
    a=a/2
   # print(a)
  else:
    a= (3*a+1)
    #print(a)
  seq.append(a)
print(seq)

