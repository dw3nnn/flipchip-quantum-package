from config import ProjectConfig
from qubit_layout import build_qubit_grid
from visualize_layout import plot_qubit_grid

def main() -> None:
    cfg = ProjectConfig()
    qubits = build_qubit_grid(cfg.qubits.nx, 
                            cfg.qubits.ny,
                            cfg.qubits.pitch_um,
                            cfg.qubits.signals)
    
    print("Example signals:", qubits["Q_0_0"].signals)
    plot_qubit_grid(qubits, "Qubit Grid + Couplings", "outputs/qubits.png")
    print("Saved outputs/qubits.png")


if __name__ == "__main__":
    main()