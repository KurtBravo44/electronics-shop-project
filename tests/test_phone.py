from src.phone import Phone
phone1 = Phone('IPhone', 9999999, 10, 2)
def test__repr__():
    assert repr(phone1) == "Phone('IPhone', 9999999, 10, 2)"