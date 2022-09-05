from typing import Dict

from ...models.bone_group_mapping import BoneGroupMapping

DEFAULT_MAPPING: Dict[str, Dict[str, BoneGroupMapping]] = {
    "Default": {
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
