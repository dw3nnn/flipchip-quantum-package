from dataclasses import dataclass
from typing import Dict, Tuple

@dataclass
class Bump:
    bid: str 
    idx: Tuple[int, int]
    pos: Tuple[float, float]
    bump_type: str
    assigned_to: str | None = None


def build_bump_grid(nx: int, ny: int, pitch_um: float) -> Dict[str, Bump]:
    """
    create an nx by ny bump lattice.
    idx = (i, j)
    pos = (i * pitch_um, j * pitch_um)
    """
    bumps: Dict[str, Bump] = {}

    for i in range(nx):
        for j in range(ny):
            bid = f"B_{i}_{j}"
            x = i * pitch_um
            y = j * pitch_um

            bumps[bid] = Bump(
                bid = bid,
                idx = (i, j),
                pos = (x, y),
                bump_type = "signal",
            )

    
    validate_bumps(bumps, nx, ny)
    return bumps

def validate_bumps(bumps: Dict[str, Bump], nx: int, ny: int) -> None:
    """
    checks
    1. Each (i, j) index is unique
    2. Indices are within [0, nx), and [0, ny)
    3. bump_type is one of the allowed strings.
    """
    allowed = {"signal", "ground", "unused"}

    seen_idx = set()
    for b in bumps.values():
        # unique idx
        if b.idx in seen_idx:
            raise ValueError(f"Duplicate bump idx detected: {b.idx}")
        seen_idx.add(b.idx)

        # in range
        i, j = b.idx
        if not (0 <= i < nx and 0 <= j < ny):
            raise ValueError(f"Bump {b.bid} has out of range idx = {b.idx} for grid {nx} x {ny}")
        
        # valid type
        if b.bump_type not in allowed:
            raise ValueError(f"Bump {b.id} has invalued bump_type='{b.bump_type}'")
