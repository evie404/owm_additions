from dataclasses import dataclass
from typing import Dict, List


@dataclass
class BoneGroupMapping:
    # name: str
    layers: List[int]
    bones: Dict[str, str]  # bone name -> human bone name
