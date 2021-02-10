from pydantic.dataclasses import dataclass
from pydantic import validator
import typing

@dataclass
class Data:
    x: float = None
    y: float = None
    kwargs: typing.Dict = None
    
    @validator ("x")
    def x_greater_than_40(x):
        if not x>=40:
            raise ValueError("Must be more than the meaning of life!")



def class_tester (class_constractor):
    test_class_1 = class_constractor()
    test_class_2 = class_constractor()

    print(f"Repr/str dunder method representation: {test_class_1}")
    print(f"Equality dunder method (using ==) (should be True if implemented): {test_class_1 == test_class_2}")
    print(f"Equality dunder method (using is) (should be True if implemented): {test_class_1 is test_class_2}")

def main ():
    test_data_point_1 = Data(30)
if __name__ == "__main__":
    main()
