# FX Stream Message for ROS 2

Custom ROS 2 message definitions for the BATCAM FX system.

To build this package, make sure all Python dependencies are installed:

```bash
pip install -r requirements.txt
```

Built and tested with Python 3.10.16 / ROS 2 Jazzy (Ubuntu 24.04 or later)
Target compatibility: ROS 2 Humble (Ubuntu 22.04 or equivalent)

# Message Types

## LevelTrigger.msg

| Type | Name |
|------|------|
| `float64` | `decibel` |

## WsAudio.msg

| Type | Name |
|------|------|
| `float64` | `gain` |
| `float32[]` | `ws` |

## LPointAudio.msg

| Type | Name |
|------|------|
| `float64` | `gain` |
| `float32[]` | `lpoint0` |
| `float32[]` | `lpoint1` |
| `float32[]` | `lpoint2` |

## Beamforming.msg

| Type | Name |
|------|------|
| `float64` | `gain` |
| `float64[]` | `bf` |
| `float64[]` | `level` |
| `int32[]` | `param1` |
| `int32[]` | `param2` |
| `int32[]` | `theta` |
| `int32[]` | `pos_x` |
| `int32[]` | `pos_y` |
| `int32[]` | `v_pos_x` |
| `int32[]` | `v_pos_y` |
