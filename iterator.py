# class mynumber:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a=self.a+1
#         return x
    
# x=mynumber()
# myiter=iter(x)
# print(next(myiter))

l1=[1,2,3,44]
myiter=iter(l1)
print(next(myiter))
print(next(myiter))