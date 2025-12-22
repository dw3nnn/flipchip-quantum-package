from dataclasses import dataclass

@dataclass(frozen=True)
class QubitSpec:
    nx: int = 4
    ny: int = 4
    pitch_um: float = 300.0 #conceptual qubit spacing

@dataclass(frozen=True)
class ProjectConfig:
    qubits: QubitSpec = QubitSpec()

    #add later specs here
