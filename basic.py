# class Person:
#     x=9

# p1=Person()
# print(p1.x)

# class Person1:
#     def __init__(self):
#         print("constructor call")

# p2=Person1()






class student:
    def __init__(self,Name,section,id,mark):
        self.name=Name
        self.Section=section
        self.id=id
        self.mark=mark
    def studentfuture(self):
        if self.mark>90:
            print("good future")
        else:
            print("bad")
    def __str__(self):
        return f"{self.name},({self.id})"

s1=student("manish","A",22,91)
s1.studentfuture()
print(s1)
# del s1
# print(s1)
# print(s1.name)

        



    

