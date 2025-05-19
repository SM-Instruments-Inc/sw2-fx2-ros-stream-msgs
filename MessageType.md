# 📄 Message Documentation

## `LevelTrigger.msg`

| Type      | Name      |
| --------- | --------- |
| `float64` | `decibel` |

## `WsAudio.msg`

| Type        | Name   |
| ----------- | ------ |
| `float64`   | `gain` |
| `float32[]` | `ws`   |

## `LPointAudio.msg`

| Type        | Name      |
| ----------- | --------- |
| `float64`   | `gain`    |
| `float32[]` | `lpoint0` |
| `float32[]` | `lpoint1` |
| `float32[]` | `lpoint2` |

## `Beamforming.msg`

| Type        | Name     |
| ----------- | -------- |
| `float64`   | `gain`   |
| `float64[]` | `bf`     |
| `float64[]` | `level`  |
| `int32[]`   | `param1` |
| `int32[]`   | `param2` |
| `int32[]`   | `theta`  |
| `int32[]`   | `posX`   |
| `int32[]`   | `posY`   |
| `int32[]`   | `vPosX`  |
| `int32[]`   | `vPosY`  |

## `Prpd.msg`

| Type        | Name       |
| ----------- | ---------- |
| `float32[]` | `noise`    |
| `float32[]` | `corona`   |
| `float32[]` | `floating` |
| `float32[]` | `surface`  |

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
