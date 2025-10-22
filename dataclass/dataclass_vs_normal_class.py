# Normal Class
class UserInfo:
    def __init__(self, name:str, age:int, gender:str):
        self.full_name = name
        self.user_age = age
        self.user_gender = gender

    def __repr__(self):
        """representation method."""
        # return f"___{self.full_name}, age: {self.user_age}, gender: {self.user_gender}"
        print(type(self.user_gender))
        return f"UserInfo2(name='{self.full_name}', age={self.user_age}, gender={self.user_gender})"
    
    def __eq__(self, value):
        """equal method."""
        if not isinstance(value, UserInfo):
            return False
        else:
            return (
                self.full_name == value.full_name and
                self.user_age == value.user_age and
                self.user_gender == value.user_gender
            )
        

# dataclass
from dataclasses import dataclass

@dataclass(order=True, frozen=True)
class UserInfo2:
    name:str
    age:int
    gender:str


# ======================================

aa = UserInfo("rayhan", 10, "Male")
bb = UserInfo2("rayhan", 10, "Male")
cc = UserInfo2("rayhan", 10, "Male")

print(aa)
print(bb)
print(cc == bb)
