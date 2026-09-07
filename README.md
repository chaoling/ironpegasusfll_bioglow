# FLL BioGlow Robot Code

Pybricks programs for the team SPIKE Prime robot. The project contains a
shared robot setup, a hub menu for selecting runs, and a standalone movement
test.

## Hardware Setup

The team robot is configured as follows:

| Port | Device | Direction |
| --- | --- | --- |
| A | Left drive motor | Counterclockwise |
| E | Right drive motor | Clockwise |
| B | Left attachment motor | Counterclockwise |
| F | Front attachment motor | Clockwise |
| C | Left color sensor | - |
| D | Right color sensor | - |

The drive base uses a 62.4 mm wheel diameter and a 130 mm axle track. If the
physical wiring changes, update the matching port or direction in
`robot.py` and `demorobot.py`.

## Files

- `robot.py`: Shared hub, drive motors, attachment motors, color sensors, and
  `DriveBase` configuration used by the menu runs.
- `main.py`: Entry point. Displays a hub menu, runs the selected program, and
  monitors the Bluetooth button for an emergency stop.
- `runs.py`: Registry of programs shown in the menu.
- `run1.py`: Forward/backward movement and left/right square tests.
- `run2.py`: Attachment motor and color sensor check.
- `demorobot.py`: Hardware setup used by the standalone base test.
- `spike_prime_base_test.py`: Runs the base movement test directly without the
  menu system.

## Local Setup

Create and activate the Python 3.14 virtual environment:

```bash
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install pybricks pybricksdev
```

The `pybricks` package supplies local API stubs. Robot programs execute on the
SPIKE Prime hub, not on the computer.

## Upload and Run

With the hub powered on and connected over Bluetooth, run from this directory:

```bash
.venv/bin/pybricksdev run ble main.py
```

The command uploads `main.py` and its imported modules, then starts the hub
menu. Select a run with the hub buttons.

To upload the standalone movement test instead:

```bash
.venv/bin/pybricksdev run ble spike_prime_base_test.py
```

Keep the robot on a clear surface before running movement tests.

## Adding A Run

Create a new module such as `run3.py` with the same async function shape as
the existing runs:

```python
async def run3(
    hub,
    robot,
    left_motor,
    right_motor,
    attachment_motor_left,
    attachment_motor_front,
):
    pass
```

Then import it and add it to `RUNS` in `runs.py`. The menu number is assigned
by its position in that tuple.
