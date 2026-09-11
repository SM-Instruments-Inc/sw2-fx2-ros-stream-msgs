# PD(Partial Discharge) point (from PD AI)

# normalized position, 0.0 ~ 1.0 (x: left -> right, y: top -> bottom)
float32 nx
float32 ny

# per-class score, 0.0 ~ 1.0, ordered by PdDetection LABEL_* constants
# [noise, corona, floating, surface], empty if not provided
float32[<=4] scores

# level at this point [dB], valid only when has_level is true
bool has_level
float32 level
