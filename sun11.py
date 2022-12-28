from student import Student
import unittest

ob = Student("raj", "sonal", 60)
class teststudent(unittest.TestCase):

        #ob = Student("raj", "sonal", 32)
       # print("\nteardown")
    def test_email(self):
        self.assertEqual(ob.email(),"raj.sonal@gmail.com")
    def test_email(self):
        print("test email")
    def test_fullname(self):
        ob1=Student("rama","rao",30)
        self.assertEqual(ob1.fullname(),"rama rao")
    def test_fullname(self):
        print("test fullname")
    def test_appy_bouns(self):
        self.assertEqual(ob.marks,60)
        ob.apply_bonus()
        self.assertEqual(ob.marks, 90)
    def test_dum(self,python):
        ob1=Student("rama","rao",30)
        ob1.dum("python")
        ob1.dum(ob1.dum,"rama raorama.rao@gmail.compython")
if __name__=="__main__":
    unittest.main()
