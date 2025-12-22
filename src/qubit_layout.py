from dataclasses import dataclass
from typing import Dict, List, Tuple

@dataclass
class Qubit:
    qid: str
    pos: Tuple[float, float] # x, y in microns
    neighbors: List[str] # nearest-neighbor couplings
    signals: List[str]

def build_qubit_grid(nx: int, ny: int, pitch_um: float) -> Dict[str, Qubit]:
    """
    Build an nx by ny qubit grid with 4 neighbor connectivity"""

    qubits: Dict[str, Qubit] = {}

    for i in range(nx):
        for j in range(ny):
            qid = f"Q_{i}_{j}"
            x = i * pitch_um
            y = j * pitch_um

            neighbors: List[str] = []
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i + di, j +dj
                if 0 <= ni < nx and 0 <= nj < ny:
                    neighbors.append(f"Q_{ni}_{nj}")

            signals = ["drive", "readout"]

            qubits[qid] = Qubit(qid=qid, pos=(x, y), neighbors=neighbors, signals=signals)

    validate_qubit_graph(qubits)
    return qubits

def validate_qubit_graph(qubits: Dict[str, Qubit]) -> None:
    """
    validation:
    - All neighbor IDs exist
    - Neighbor relation is symmetric (undirected coupling graph)
    """
    ids = set(qubits.keys())

    #neighbors must exist
    for q in qubits.values():
        for nb in q.neighbors:
            if nb not in ids:
                raise ValueError(f"{q.qid} has neighbor {nb} that does not exist")

    #symmetry
    for q in qubits.values():
        for nb in q.neighbors:
            if q.qid not in qubits[nb].neighbors:
                raise ValueError(f"Neighbor symmetry violated: {q.qid} lists {nb} but not vice versa")