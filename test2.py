from enum import Enum, EnumMeta


class IntEnumMeta(EnumMeta):
    def __new__(cls, name, bases, attrs):
        member_names = [member_name for member_name in attrs._member_names.keys()]
        member_dict = {member_name: attrs[member_name] for member_name in member_names}

        for member_name, member_value in member_dict.items():
            if not isinstance(member_value, int):
                raise ValueError(f"{name}.{member_name} must be an integer")
        return super().__new__(cls, name, bases, attrs)


class IntEnum(Enum, metaclass=IntEnumMeta):
    pass


class MyEnum(IntEnum):
    VALUE1 = 1
    VALUE2 = 2


print(MyEnum.VALUE2.value)
