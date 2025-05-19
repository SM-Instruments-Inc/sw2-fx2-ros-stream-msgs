# 📄 Message Documentation

## `LevelTrigger.msg`

| Type      | Name      |
| --------- | --------- |
| `float64` | `decibel` |

## `WsAudio.msg`

| Type            | Name   |
| --------------- | ------ |
| `float64`       | `gain` |
| `float32[8000]` | `ws`   |

## `LPointAudio.msg`

| Type            | Name      |
| --------------- | --------- |
| `float64`       | `gain`    |
| `float32[8000]` | `lpoint0` |
| `float32[8000]` | `lpoint1` |
| `float32[8000]` | `lpoint2` |

## `Beamforming.msg`

| Type            | Name     |
| --------------- | -------- |
| `float64`       | `gain`   |
| `float64[1200]` | `bf`     |
| `float64[5]`    | `level`  |
| `int32[5]`      | `param1` |
| `int32[5]`      | `param2` |
| `int32[5]`      | `theta`  |
| `int32[5]`      | `posX`   |
| `int32[5]`      | `posY`   |
| `int32[5]`      | `vPosX`  |
| `int32[5]`      | `vPosY`  |

## `Prpd.msg`

| Type         | Name       |
| ------------ | ---------- |
| `float32[3]` | `noise`    |
| `float32[3]` | `corona`   |
| `float32[3]` | `floating` |
| `float32[3]` | `surface`  |

## `BeamformingSetting.msg`

| Type      | Name        |
| --------- | ----------- |
| `bool`    | `autogain`  |
| `float64` | `gain`      |
| `float64` | `x_cal`     |
| `float64` | `y_cal`     |
| `float64` | `distance`  |
| `float64` | `high_cut`  |
| `float64` | `low_cut`   |
| `int32`   | `l_point_0` |
| `int32`   | `l_point_1` |
| `int32`   | `l_point_2` |

## `OverlaySetting.msg`

| Type    | Name         |
| ------- | ------------ |
| `bool`  | `enable`     |
| `bool`  | `findsource` |
| `int32` | `maxsource`  |
| `int32` | `average`    |
| `int32` | `threshold`  |
| `int32` | `range`      |
