from business.loginPage import LoginPage
from business.addEmployee import AddEmployee


class TestAddEmp:
    def test_add_emp(self, my_fixture):
        loginpage = LoginPage(my_fixture)
        loginpage.login()
        addemp = AddEmployee(my_fixture)
        addemp.add_employee("杉杉", "shanshan", "15800000002")
        assert addemp.check_add_employee() is True


