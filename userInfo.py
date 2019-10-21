class userInfo:
    def getInfo(self):
        self.usn=int(input("Enter your usn: "))
        self.name=input("Enter your name:  ")
        self.age=int(input("Enter the age: "))

    def printInfo(self):
        print("USN: ",self.usn)
        print("Name: ",self.name)
        print("Age: ",self.age)

u=userInfo()
u.getInfo()
u.printInfo()