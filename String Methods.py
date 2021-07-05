"""
    1)Capitalize()
    2)casefold()
    3)center()
    4)count()
    5)endswidth()
    6)find()
    8)format()
    9)index()
    10)isdigit()
    11)islower()
    12)isupper()
    13)join()
    14)lower()
    15)upper()
    16)replace()
    17)swapcase()
    18)split()
    19)title()
    20)startwith()
"""


data="python language"
out=data.capitalize()
print("Capitalize Word:",out)


data="Python Language"
out=data.casefold()
print("Casefold:",out)


data="Python Language"
out=data.center(50)
print("Center:",out)


data="Python Python Language"
out=data.count("Python")
print("Count:",out)


data="Python Python Language"
out=data.endswith(".")
print("Endswith:",out)

data="Python Language."
out=data.find("Language")
print("Find:",out)


data="Python {} Language."
out=data.format("is a")
print("Format:",out)


data="Python Language."
out=data.index("Language")
print("Index:",out)


data="34s23"
out=data.isdigit()
print("Isdigit:",out)


data="Python"
out=data.islower()
print("Islower:",out)

data="PYTHON"
out=data.isupper()
print("Isupper:",out)

data=("Python","Porgramming","Language")
out="*".join(data)
print("Join:",out)

data="PYTHON"
out=data.lower()
print("Lower:",out)


data="python"
out=data.upper()
print("Upper:",out)


data="Python Language"
out=data.replace("Python","HTML")
print("Replace:",out)


data="Python Language"
out=data.split()
print("Split:",out)



data="python language"
out=data.title()
print("Title:",out)


data="Python language"
out=data.startswith("P")
print("Startswith:",out) 



