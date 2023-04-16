from dataclasses import dataclass
from enum import Enum

from .validator_enum import _ValidatorEnumMeta


class _CommandEnumMeta(_ValidatorEnumMeta):
    def __new__(cls, name, bases, classdict):
        cls._validate_types(classdict, desired_type=Command)
        return super().__new__(metacls=cls, cls=name, bases=bases, classdict=classdict)


@dataclass
class Command:
    name: str
    serial_command: int
    number_of_data_bytes: int = 0


class CommandEnum(Enum, metaclass=_CommandEnumMeta):
    @property
    def name(self):
        return self.value.name

    @property
    def serial_command(self):
        return self.value.serial_command

    @property
    def number_of_data_bytes(self):
        return self.value.number_of_data_bytes
