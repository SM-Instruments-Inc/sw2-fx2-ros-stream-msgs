# Leak point (from LEAK AI)

# normalized position, 0.0 ~ 1.0 (x: left -> right, y: top -> bottom)
float32 nx
float32 ny

# score, 0.0 ~ 1.0, valid only when has_score is true
bool has_score
float32 score

# level at this point [dB], valid only when has_level is true
bool has_level
float32 level
