from typing import Dict

from ...bone_group_mapping import BoneGroupMapping

CLASSIC_MAPPING: Dict[str, Dict[str, BoneGroupMapping]] = {
    "Classic": {
        "Hair": BoneGroupMapping(
            [19],
            {},
        ),
        "Wings": BoneGroupMapping(
            [8],
            {},
        ),
        "Body Flaps": BoneGroupMapping(
            [24],
            {},
        ),
        "Body Fins": BoneGroupMapping(
            [25],
            {},
        ),
    },
}
