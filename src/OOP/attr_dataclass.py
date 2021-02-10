import typing
from dataclasses import dataclass

import attr


class Data_plain:
    def __init__(self, x: float=None, y:float=None, kwargs:typing.Dict=None):
        self.x = x
        self.y = y
        self.kwargs = kwargs

def class_tester (class_constractor):
    test_class_1 = class_constractor()
    test_class_2 = class_constractor()

    print(f"Repr/str dunder method representation: {test_class_1}")
    print(f"Equality dunder method (using ==) (should be True if implemented): {test_class_1 == test_class_2}")
    print(f"Equality dunder method (using is) (should be True if implemented): {test_class_1 is test_class_2}")

@dataclass
class Data_DataClass:
    x: float = None
    y: float = None
    kwargs: typing.Dict = None

@attr.s
class Data_attr:
    x: float = attr.ib(default=None)
    y: float = attr.ib(default=None)
    kwargs: typing.Dict = attr.ib(default=None)

@attr.s
class ValidatedData:
    x:float = attr.ib(default = None,validator = attr.validators.instance_of(int))
    y:float = attr.ib(default=None)
    kwargs: typing.Dict = attr.ib(default=None)

    @x.validator
    def more_than_the_meaning_of_life(self, attribute, value):
        if not value >= 42:
          raise ValueError("Must be more than the meaning of life!")

@attr.s
class ConvertedData:
    x: float = attr.ib(default=None,converter=int)
    y: float = attr.ib(default=None)
    kwargs: typing.Dict = attr.ib(default=None)

    @x.validator
    def more_than_the_meaning_of_life(self, attribute, value):
        if not value >= 42:
            raise ValueError("Must be more than the meaning of life!")
    
     
def main ():
    # class_tester(Data_plain)
    # class_tester(Data_DataClass)
    # class_tester(Data_attr)
    # print ("testing data_point_1")
    # test_data_point_1 = ValidatedData(42)
    # print ("testing data_point_2")
    # test_data_point_2 = ValidatedData(-35) 

    print ("testing converted data_point_1")
    test_data_point_1 = ConvertedData(42)
    print ("testing converted data_point_2")
    #test_data_point_2 = ConvertedData(-35) 
if __name__ == "__main__":
    main()

