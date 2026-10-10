import pytest
from Exceptions import ExceptionsDemo, MyException  

@pytest.mark.unit
def test_divide_zero():
    demo = ExceptionsDemo()
    with pytest.raises(ZeroDivisionError):
        demo.divide(10,0)

@pytest.mark.unit 
def test_TypeError():
    demo = ExceptionsDemo()
    with pytest.raises(TypeError):
        demo.divide("Tamaulipas",0)

@pytest.mark.unit
def test_index_error():
    demo = ExceptionsDemo()
    with pytest.raises(IndexError):
        demo.access_list([3,5,4],7)    

@pytest.mark.unit
def test_index_type_error():
    demo = ExceptionsDemo()
    with pytest.raises((TypeError, IndexError)):
        demo.access_list([3,5,4],1)   
        demo.access_list([3,5,4],7)
        demo.access_list([3,5,4],"5")

@pytest.mark.unit
def test_FileNotFound_error():
    demo = ExceptionsDemo()
    with pytest.raises(FileNotFoundError):
        demo.read_file("frutas.txt")

@pytest.mark.unit
def test_attribute_error():
    demo = ExceptionsDemo()
    demoFake = ExceptionsDemo()
    with pytest.raises(AttributeError):
        demo.access_attribute(demoFake)

@pytest.mark.wip
def test_my_exception_error():
    demo = ExceptionsDemo()
    with pytest.raises(MyException):
        demo.check_positive(-3)
