import unittest
from student import Student
ob=Student("rajya","lakshmi",30)
ob1=Sudent("rajya","lakshmi",30)
ob2=Student("raj","ya",30)

class teststudent(unittest.TestCase):
    def test_email(self):
        self.assertEqual(ob.email(),'rajya.lakshmi@gmail.com')
    def test_apply_bonus(self):
        self.assertEqual(ob1.apply_bouns(),45)
    def test_fullname(self):
        self.assertEqual(ob2.fullname(),"rajya")

if __name__=="__main__":
    unittest.main()
