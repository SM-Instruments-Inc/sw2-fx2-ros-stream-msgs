# 📄 Message Documentation

## `Beamforming.msg`

| Type | Name |
|------|------|
| `float64` | `gain` |
| `float64[1200]` | `bf` |
| `float64[5]` | `level` |
| `int32[5]` | `param1` |
| `int32[5]` | `param2` |
| `int32[5]` | `theta` |
| `int32[5]` | `pos_x` |
| `int32[5]` | `pos_y` |
| `int32[5]` | `v_pos_x` |
| `int32[5]` | `v_pos_y` |

## `BeamformingSetting.msg`

| Type | Name |
|------|------|
| `bool` | `autogain` |
| `float64` | `gain` |
| `float64` | `x_cal` |
| `float64` | `y_cal` |
| `float64` | `distance` |
| `float64` | `high_cut` |
| `float64` | `low_cut` |
| `int32` | `l_point_0` |
| `int32` | `l_point_1` |
| `int32` | `l_point_2` |

## `LPointAudio.msg`

| Type | Name |
|------|------|
| `float64` | `gain` |
| `float32[]` | `lpoint0` |
| `float32[]` | `lpoint1` |
| `float32[]` | `lpoint2` |

## `LeakDetection.msg`

| Type | Constant | Value |
|------|----------|-------|
| `uint8` | `STATE_DISABLED` | `0` |
| `uint8` | `STATE_WARMUP` | `1` |
| `uint8` | `STATE_ENABLED` | `2` |
| `uint8` | `LABEL_NOISE` | `0` |
| `uint8` | `LABEL_LEAK` | `1` |

| Type | Name |
|------|------|
| `builtin_interfaces/Time` | `stamp` |
| `uint8` | `state` |
| `uint8` | `label` |
| `bool` | `has_confidence` |
| `float32` | `confidence` |
| `LeakSource[]` | `sources` |

## `LeakSource.msg`

| Type | Name |
|------|------|
| `float32` | `nx` |
| `float32` | `ny` |
| `bool` | `has_score` |
| `float32` | `score` |
| `bool` | `has_level` |
| `float32` | `level` |

## `LevelTrigger.msg`

| Type | Name |
|------|------|
| `float64` | `decibel` |

## `OverlaySetting.msg`

| Type | Name |
|------|------|
| `bool` | `enable_overlay` |
| `bool` | `enable_source_mode` |
| `int32` | `number_of_sources` |
| `int32` | `average` |
| `float64` | `threshold` |
| `float64` | `range` |

## `Prpd.msg`

| Type | Name |
|------|------|
| `float32[3]` | `noise` |
| `float32[3]` | `corona` |
| `float32[3]` | `floating` |
| `float32[3]` | `surface` |

## `PrpdDetection.msg`

| Type | Constant | Value |
|------|----------|-------|
| `uint8` | `STATE_DISABLED` | `0` |
| `uint8` | `STATE_WARMUP` | `1` |
| `uint8` | `STATE_ENABLED` | `2` |
| `uint8` | `LABEL_NOISE` | `0` |
| `uint8` | `LABEL_CORONA` | `1` |
| `uint8` | `LABEL_FLOATING` | `2` |
| `uint8` | `LABEL_SURFACE` | `3` |

| Type | Name |
|------|------|
| `builtin_interfaces/Time` | `stamp` |
| `uint8` | `state` |
| `uint8` | `label` |
| `bool` | `has_confidence` |
| `float32` | `confidence` |
| `PrpdSource[]` | `sources` |

## `PrpdSource.msg`

| Type | Name |
|------|------|
| `float32` | `nx` |
| `float32` | `ny` |
| `float32[<=4]` | `scores` |
| `bool` | `has_level` |
| `float32` | `level` |

## `WsAudio.msg`

| Type | Name |
|------|------|
| `float64` | `gain` |
| `float32[]` | `ws` |
