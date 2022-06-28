# conding = utf-8
import os

f = open(os.path.dirname(__file__)+"/11.png","rb")

with open(os.path.dirname(__file__)+"/234.png","wb") as fl:
    # print(f.read())
    content=f.read()
    fl.write(content)
    print(content)
    fl.close()
f.close()