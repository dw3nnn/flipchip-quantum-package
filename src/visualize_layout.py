import os
from typing import Dict
import matplotlib.pyplot as plt
from qubit_layout import Qubit

def plot_qubit_grid(qubits: Dict[str, Qubit], title: str, savepath: str) -> None:
    os.makedirs(os.path.dirname(savepath), exist_ok=True)

    plt.figure()

    # plot qubit points
    qx = [q.pos[0] for q in qubits.values()]
    qy = [q.pos[1] for q in qubits.values()]
    plt.scatter(qx, qy, s=60, label="qubits")

    # plot couplings (avoid double-drawing)
    for q in qubits.values():
        for nb in q.neighbors:
            if q.qid < nb:
                x1, y1 = q.pos
                x2, y2 = qubits[nb].pos
                plt.plot([x1, x2], [y1, y2], linewidth=1)

    plt.title(title)
    plt.xlabel("x (um)")
    plt.ylabel("y (um)")
    plt.axis("equal")
    plt.tight_layout()
    plt.legend()
    plt.savefig(savepath, dpi=200)
    plt.close()
