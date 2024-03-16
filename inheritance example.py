class Faculty:
    def __init__(self,f_name,department,f_id):
        self.f_name=f_name
        self.department=department
        self.f_id=f_id
    def print_info(self):
        print('faculty information=',self.f_name,self.department,self.f_id)
obj=Faculty("asish","computer_science",1001)
obj.print_info()


"""
class cse(Faculty):
pass
obj=cse("jyoti","computer_scinece",1002)
obj.print_info()
"""
