from dataclasses import dataclass


@dataclass
class SensorPacket:
    packet_id: int
    number_of_bytes: int
    signed: bool
