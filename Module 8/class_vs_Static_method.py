class Student:
    uni_name = 'Niter'

    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id

    def stu_detail(self):
        print(f'Name: {self.name} id: {self.id} Uni_name: {Student.uni_name}')
    @classmethod
    def up_uni_name(cls, u_name):
        Student.uni_name = u_name

s1 = Student('samiul', 56)
s2 = Student('rownok',45)
s1.stu_detail()
s2.stu_detail()
Student.up_uni_name('National Institute of Textile Engineering and Reaserch')
s1.stu_detail()
s2.stu_detail()

# ===============static method=================
class Friend:
    @staticmethod
    def two_friend(name1,name2):
        return name1 + name2

result = Friend.two_friend('samiul ','rownok')
print(result)