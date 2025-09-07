class Hospital:
    def __init__(self,patientName,address,mobileNumber,age):
        print("hii")
        self.patientName=patientName
        self.address=address
        self.mobileNumber=mobileNumber
        self.age=age
        self.lst=["OPD","IPD","Emergency"]
    def __str__(self):
        return f"{self.patientName}"
  
        

    
class patientDepartment(Hospital):
    def __init__(self, patientName, address, mobileNumber, age, departmentName, Doctorname, diagonises):
        # Hospital.__init__(self,patientName,address,mobileNumber,age)
        super().__init__(patientName,address,mobileNumber,age)
        self.patientName="Prince kumar"
        self.departmentName=departmentName
        self.Doctorname=Doctorname
        self.diagonises=diagonises
    def Services(self):
        if self.age>80:
            print(self.patientName)
            print(self.lst[2])
        else:
            print(self.patientName)
            print(self.lst[1])

p=patientDepartment("prince","ssm","7123122",555,"orthopedics","vivek","body pain")
p.Services()
