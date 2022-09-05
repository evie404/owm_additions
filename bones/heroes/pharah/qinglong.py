from typing import Dict

from ...bone_group_mapping import BoneGroupMapping

QINGLONG_MAPPING: Dict[str, Dict[str, BoneGroupMapping]] = {
    "Qinglong": {
        "Hair": BoneGroupMapping(
            [19],
            {
                "bone_0083": "",
                "bone_05DA": "",
                "bone_05DB": "",
                "bone_01A0": "",
                "bone_00AB": "",
                "bone_00A3": "",
                "bone_01A1": "",
                "bone_00AC": "",
                "bone_00A4": "",
                "bone_01A2": "",
                "bone_019A": "",
                "bone_00A5": "",
                "bone_01A3": "",
                "bone_019B": "",
                "bone_00A6": "",
                "bone_01A4": "",
                "bone_019C": "",
                "bone_00A7": "",
                "bone_01A5": "",
                "bone_019D": "",
                "bone_00A8": "",
                "bone_01A6": "",
                "bone_019E": "",
                "bone_00A9": "",
                "bone_01A7": "",
                "bone_019F": "",
                "bone_00AA": "",
            },
        ),
        "Wings": BoneGroupMapping(
            [8],
            {
                "bone_0122": "",
                "bone_011E": "",
                "bone_011F": "",
                "bone_0123": "",
                "bone_0120": "",
                "bone_0121": "",
            },
        ),
        "Wrist Adjustments": BoneGroupMapping(
            [15],
            {"bone_00A1": "", "bone_00A2": ""},
        ),
        "Left Arm Rocket": BoneGroupMapping(
            [9],
            {"bone_0140": ""},
        ),
        "Shoulder Guards": BoneGroupMapping(
            [24],
            {"bone_007B": "", "bone_0089": "", "bone_007A": "", "bone_008A": ""},
        ),
        "Leg Guards": BoneGroupMapping(
            [25],
            {
                "bone_0159": "",
                "bone_0158": "",
                "bone_012E": "",
                "bone_01C1": "",
                "bone_01B9": "",
                "bone_01BB": "",
                "bone_01BC": "",
                "bone_01BD": "",
                "bone_01BE": "",
                "bone_01BF": "",
                "bone_01D7": "",
                "bone_01D8": "",
                "bone_01D9": "",
                "bone_01DA": "",
                "bone_01DB": "",
                "bone_01DC": "",
                "bone_01DD": "",
                "bone_013E": "",
                "bone_008C": "",
                "bone_013B": "",
                "bone_012D": "",
                "bone_0255": "",
                "bone_0254": "",
                "bone_0253": "",
                "bone_0252": "",
                "bone_0251": "",
                "bone_0250": "",
                "bone_024F": "",
                "bone_020A": "",
                "bone_020B": "",
                "bone_020C": "",
                "bone_020D": "",
                "bone_020E": "",
                "bone_020F": "",
                "bone_0210": "",
                "bone_013D": "",
                "bone_008D": "",
                "bone_013C": "",
            },
        ),
        "Helmet (Detached)": BoneGroupMapping(
            [26],
            {
                "bone_0731": "",
                "bone_0592": "",
                "bone_006C": "",
            },
        ),
        "Helmet (Full)": BoneGroupMapping(
            [27],
            {
                "bone_0011": "",
                "bone_0012": "",
                "bone_006A": "",
            },
        ),
        "Hair (Unused)": BoneGroupMapping(
            [14],
            {
                # beads
                "bone_07A9": "",
                "bone_07AA": "",
                "bone_07AB": "",
                "bone_07B3": "",
                "bone_07B4": "",
                "bone_07B5": "",
                # other unused hair parts
                "bone_0084": "",
                "bone_05DC": "",
            },
        ),
    },
}
