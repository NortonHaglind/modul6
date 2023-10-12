active=True

operator=["+","-","*","/","^","%"]
def error():
  print("skriv rätt")

def count(x,y,op="+"):
  if op=="+":
    return x + y
  elif op=="-":
    return x-y
  elif op=="*":
    return x*y
  elif op=="/":
    return x/y
  elif op=="^":
    return x**y
  elif op=="%":
    return x%y
  
  


#def name():
  #  return("nmanren")

#for i in range (1,10):
#  print(name())


def edit(editnumber, editname):
  namelist[editnumber-1]=editname
  print(namelist)
  print(len(namelist))
  
def remove(editnumber):
  namelist.pop(editnumber-1)   
  print(namelist)
  print(len(namelist))                 



namelist=[]
while active:
  name=input("skriv nåt roligt (sluta=q)(ta bort=x)(edit=e) ")
  if name=="e":
    while True:
      try:
        editnumber=int(input(f"vilken vil du ändra"))
        if 1<=editnumber<=len(namelist):
          editname=input(f"vad vill du skriva")
          edit(editnumber, editname)
        else:
          continue
        break
      except:
        continue
  elif name=="q":
    active=False
  elif name=="x":
    while True:
      try:
        editnumber=int(input(f"vilken vill du ta bort"))
        if 1<=editnumber<=len(namelist):
          remove(editnumber)
        else:
          continue

        break
      except:
        continue
  else:
    namelist.append(name)
    print(namelist)
    print(len(namelist))


while True:
  try:
    x=int(input("skriv första tal "))
    break
  except:
    error()
    continue
while True:  
  try:
    y=int(input("skriv andra tal "))
    break
  except:
    error()
    continue
while True:
  op=input("vilket räknesätt? ")
  if op in operator:
    count(x,y,op)
    print(count(x,y,op))
    break
  else:
    error()
    continue
