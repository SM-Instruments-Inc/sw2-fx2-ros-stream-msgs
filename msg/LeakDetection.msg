# Leak detection event
# Detection (multi-frame accumulation, threshold, hysteresis) is done by the
# inference engine on the device; this message carries only the conclusion.

# acquisition time of the frame this conclusion was drawn from
builtin_interfaces/Time stamp

# state
uint8 STATE_DISABLED = 0    # LEAK AI off
uint8 STATE_WARMUP   = 1    # on, not enough accumulation yet (undetermined)
uint8 STATE_ENABLED  = 2    # LEAK AI on

# label
uint8 LABEL_NOISE = 0
uint8 LABEL_LEAK  = 1

uint8 state
uint8 label

# detection confidence, 0.0 ~ 1.0 (NOT a single-frame model score)
# valid only when has_confidence is true
bool has_confidence
float32 confidence

# may be empty when no source is available;
# current hardware emits at most 5, but the count is intentionally
# left unbounded so consumers need not be rebuilt if that changes
LeakSource[] sources
