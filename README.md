# Serialroomba

Serialroomba is a package that aims to simplify the control of a Roomba over its serial port.

It was tested on a Roomba 570.

Similar packages already exist, some relatively old, some too "low-level".  
Part of the goal of this package was also to practice Python OOP.  

## Usage

To install this package, you simply need to `pip install serialroomba`

Here is an example script:
```python
from serialroomba.serialroomba import SerialRoomba
from serialroomba.controllers import CleaningMode, Mode

roomba = SerialRoomba("/dev/ttyS0")
roomba.mode_controller.current_mode = Mode.SAFE
roomba.cleaning_controller.side_brush_pwm = 10
roomba.mode_controller.current_mode = Mode.PASSIVE
roomba.cleaning_controller.current_cleaning_mode = CleaningMode.SPOT
```

## Not implemented

### Motors (Opcode: 138)

"This command lets you control the forward and backward motion of Roomba’s main brush, side brush,
and vacuum independently."  
Since the state and direction of all cleaning motors need to be sent in a single byte,
managing the last state of them becomes complicated.  
The same functionality can be achieved using:

- main_brush_pwm
- side_brush_pwm
- vacuum_pwm

### LEDs (Opcode: 139)

"This command controls the LEDs common to all models of Roomba 500."

### Scheduling LEDs (Opcode: 162)

"This command controls the state of the scheduling LEDs present on the Roomba 560 and 570."

### Digital LEDs Raw (Opcode: 163)

"This command controls the four 7 segment displays on the Roomba 560 and 570."

### Digit LEDs ASCII (Opcode: 164)

"This command controls the four 7 segment displays on the Roomba 560 and 570 using ASCII character codes."

### Buttons (Opcode: 165)

"This command lets you push Roomba’s buttons. The buttons will automatically release after 1/6th of a
second."

### Song (Opcode: 140)

"This command lets you specify up to four songs to the OI that you can play at a later time. Each song is
associated with a song number."

### Play (Opcode: 141)

"This command lets you select a song to play from the songs added to Roomba using the Song command."
