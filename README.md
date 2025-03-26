# FX Stream Message for ROS 2

Custom ROS 2 message definitions for BATCAM FX.

# Message Types

# 📄 Message Documentation

## `LevelTrigger.msg`

| Type | Name |
|------|------|
| `float64` | `decibel` |

## `WsAudio.msg`

| Type | Name |
|------|------|
| `float64` | `gain` |
| `float32[]` | `ws` |

## `LPointAudio.msg`

| Type | Name |
|------|------|
| `float64` | `gain` |
| `float32[]` | `lpoint0` |
| `float32[]` | `lpoint1` |
| `float32[]` | `lpoint2` |

## `Beamforming.msg`

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
