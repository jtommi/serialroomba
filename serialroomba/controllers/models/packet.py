from dataclasses import dataclass
from serialroomba.controllers.serial import DataTypes


@dataclass
class SensorPacket:
    packet_id: int
    data_type: DataTypes
