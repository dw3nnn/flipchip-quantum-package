from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class QubitSpec:
    nx: int = 4
    ny: int = 4
    pitch_um: float = 300.0 #conceptual qubit spacing

    signals: List[str] = field(default_factory=lambda: ["drive", "readout", "flux bias"])


@dataclass(frozen=True)
class ProjectConfig:
    qubits: QubitSpec = QubitSpec()

    #add later specs here
