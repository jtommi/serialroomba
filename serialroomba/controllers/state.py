from __future__ import annotations


from dataclasses import dataclass
from enum import Enum, EnumMeta


class StateEnumMeta(EnumMeta):
    def __new__(cls, name, bases, classdict):
        member_names = [member_name for member_name in classdict._member_names.keys()]
        member_dict = {
            member_name: classdict[member_name] for member_name in member_names
        }

        for member_name, member_value in member_dict.items():
            if not isinstance(member_value, State):
                raise TypeError(f"{name}.{member_name} is not a valid State")
        return super().__new__(metacls=cls, cls=name, bases=bases, classdict=classdict)


@dataclass
class State:
    name: str
    command: int | None
    state_id: int


class StateEnum(Enum, metaclass=StateEnumMeta):
    @property
    def name(self):
        return self.value.name

    @property
    def command(self):
        return self.value.command

    @property
    def state_id(self):
        return self.value.state_id

    @classmethod
    def from_state_id(cls, state_id) -> StateEnum:
        for state in cls:
            if state.state_id == state_id:
                return cls(state)

        raise KeyError(f"State with ID {state_id} not defined")
