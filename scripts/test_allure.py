import pytest

class Test_Allure:
    
    def setup_class(self):
        print("setup_class")
    def teardown_class(self):
        print("teardown_class")
        
    def test_allure(self):
        print("test_allure")
        assert True