from typing import Dict

from ...bone_group_mapping import BoneGroupMapping

BASE_MAPPING: Dict[str, Dict[str, BoneGroupMapping]] = {
    "Base": {
        "Helmet (Detached)": BoneGroupMapping(
            [26],
            {
                "bone_0592": "Helmet (Detached)",
            },
        ),
        "Helmet (Full)": BoneGroupMapping(
            [27],
            {
                "bone_0012": "Helmet (Full)",
            },
        ),
        "Wings": BoneGroupMapping(
            [8],
            {
                "bone_011E": "Wing Outer L",
                "bone_011F": "Wing Inner L",
                "bone_0120": "Wing Outer R",
                "bone_0121": "Wing Inner R",
                "bone_0122": "Wing L",
                "bone_0123": "Wing R",
            },
        ),
        "Armors": BoneGroupMapping(
            [24],
            {
                "bone_007A": "Shoulder Armor R",
                "bone_007B": "Shoulder Armor L",
                "bone_0089": "Shoulder Armor Cover L",
                "bone_008A": "Shoulder Armor Cover R",
                "bone_008C": "Leg Upper Cover L",
                "bone_008D": "Leg Upper Cover R",
                "bone_013D": "Leg Lower Cover R",
                "bone_013E": "Leg Lower Cover L",
                # not found in all
                "bone_012D": "Leg Knee Cover R",
                "bone_012E": "Leg Knee Cover L",
            },
        ),
        "Munitions": BoneGroupMapping(
            [25],
            {
                "bone_013B": "Leg Rockets L",
                "bone_013C": "Leg Rockets R",
                "bone_0140": "Concussion Rocket",
            },
        ),
        "Wrist Adjustments": BoneGroupMapping(
            [15],
            {
                # not found in all
                "bone_00A1": "Wrist Adjustment L",
                "bone_00A2": "Wrist Adjustment R",
            },
        ),
    },
}
