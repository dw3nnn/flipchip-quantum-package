from typing import Dict
from src.bumps import Bump

def apply_checkerboard(bumps: Dict[str, Bump]) -> None:
    """
    Assign bump type using a checkerboard patter
    ( i + j) even -> ground
    (i + j) odd -> signal
    
    ensure strong local return paths / shielding for signal bumps
    """

    for b in bumps.values():
        i, j = b.idx
        if (i + j) % 2 == 0:
            b.bump_type = "ground"
        else:
            b.bump_type = "signal"


def apply_stripes(bumps: Dict[str, Bump], k: int = 3, axis: str = "x") -> None:
    """
    Assign bump_type using a stripes pattern:
      - Every k-th line along the chosen axis becomes ground.
      - Other bumps become signal.

    axis="x" means: columns i = 0, k, 2k, ... are ground
    axis="y" means: rows    j = 0, k, 2k, ... are ground

    This pattern is routing-friendly: ground "rails" run across the grid.
    """
    axis = axis.lower()
    if axis not in ("x", "y"):
        raise ValueError("axis must be 'x' or 'y' ")
    if k < 1:
        raise ValueError(" k must be >= 1")
    

    for b in bumps.values():
        i, j = b.idx
        ref = i if axis == "x" else j

        if ref % k == 0:
            b.bump_type = "ground"

        else:
            b.bump_type = "signal"

