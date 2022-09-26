from typing import Dict

from ...bone_group_mapping import BoneGroupMapping

CLASSIC_MAPPING: Dict[str, Dict[str, BoneGroupMapping]] = {
    "Classic": {
        "Body Flaps": BoneGroupMapping(
            [24],
            {
                "bone_00A3": "Front Flap Root",
                "bone_00B1": "Front Flap 1 1",
                "bone_00B3": "Front Flap 1 2",
                "bone_00BE": "Front Flap 1 3",
                "bone_00A7": "Front Flap 1 4",
                "bone_00BF": "Front Flap 1 5",
                "bone_00B8": "Front Flap 1 6",
                "bone_019C": "Front Flap 1 7",
                "bone_00BA": "Front Flap 1 8",
                "bone_019F": "Front Flap 1 9",
                "bone_00BC": "Front Flap 1 10",
                "bone_01B8": "Front Flap 1 11",
                "bone_01BC": "Front Flap 1 12",
                "bone_01CB": "Front Flap 1 13",
                "bone_01C6": "Front Flap 1 14",
                "bone_00A5": "Front Flap 2 1",
                "bone_00A6": "Front Flap 2 2",
                "bone_00BD": "Front Flap 2 3",
                "bone_00B5": "Front Flap 2 4",
                "bone_00C0": "Front Flap 2 5",
                "bone_00B7": "Front Flap 2 6",
                "bone_019A": "Front Flap 2 7",
                "bone_00A9": "Front Flap 2 8",
                "bone_019D": "Front Flap 2 9",
                "bone_00AA": "Front Flap 2 10",
                "bone_01B6": "Front Flap 2 11",
                "bone_01B9": "Front Flap 2 12",
                "bone_01BF": "Front Flap 2 13",
                "bone_01C4": "Front Flap 2 14",
                "bone_00B4": "Front Flap 3 1",
                "bone_00B6": "Front Flap 3 2",
                "bone_00AB": "Front Flap 3 3",
                "bone_00A8": "Front Flap 3 4",
                "bone_00AC": "Front Flap 3 5",
                "bone_00B9": "Front Flap 3 6",
                "bone_019B": "Front Flap 3 7",
                "bone_00BB": "Front Flap 3 8",
                "bone_019E": "Front Flap 3 9",
                "bone_00B0": "Front Flap 3 10",
                "bone_01B7": "Front Flap 3 11",
                "bone_01BB": "Front Flap 3 12",
                "bone_01C0": "Front Flap 3 13",
                "bone_01C5": "Front Flap 3 14",
                "bone_01A3": "Front Flap 4 1",
                "bone_01A5": "Front Flap 4 2",
                "bone_01AF": "Front Flap 4 3",
                "bone_01A7": "Front Flap 4 4",
                "bone_01B0": "Front Flap 4 5",
                "bone_01A9": "Front Flap 4 6",
                "bone_01B2": "Front Flap 4 7",
                "bone_01AB": "Front Flap 4 8",
                "bone_01B4": "Front Flap 4 9",
                "bone_01AD": "Front Flap 4 10",
                "bone_01BA": "Front Flap 4 11",
                "bone_01BD": "Front Flap 4 12",
                "bone_01C2": "Front Flap 4 13",
                "bone_01C7": "Front Flap 4 14",
                "bone_01A4": "Front Flap 5 1",
                "bone_01A6": "Front Flap 5 2",
                "bone_01AE": "Front Flap 5 3",
                "bone_01A8": "Front Flap 5 4",
                "bone_01B1": "Front Flap 5 5",
                "bone_01AA": "Front Flap 5 6",
                "bone_01B3": "Front Flap 5 7",
                "bone_01AC": "Front Flap 5 8",
                "bone_01B5": "Front Flap 5 9",
                "bone_01A1": "Front Flap 5 10",
                "bone_01C1": "Front Flap 5 11",
                "bone_01BE": "Front Flap 5 12",
                "bone_01C3": "Front Flap 5 13",
                "bone_01C8": "Front Flap 5 14",
                # Back
                "bone_00A4": "Back Flap Root",
                "bone_01CA": "Back Flap 1 1",
                "bone_01E0": "Back Flap 1 2",
                "bone_01D1": "Back Flap 1 3",
                "bone_01E4": "Back Flap 1 4",
                "bone_01D2": "Back Flap 1 5",
                "bone_01E8": "Back Flap 1 6",
                "bone_01D6": "Back Flap 1 7",
                "bone_01EB": "Back Flap 1 8",
                "bone_01C9": "Back Flap 1 9",
                "bone_0210": "Back Flap 1 10",
                "bone_0217": "Back Flap 1 11",
                "bone_021E": "Back Flap 1 12",
                "bone_0225": "Back Flap 1 13",
                "bone_01CC": "Back Flap 2 1",
                "bone_01DD": "Back Flap 2 2",
                "bone_01CF": "Back Flap 2 3",
                "bone_01E1": "Back Flap 2 4",
                "bone_01D4": "Back Flap 2 5",
                "bone_01E5": "Back Flap 2 6",
                "bone_01D8": "Back Flap 2 7",
                "bone_01F3": "Back Flap 2 8",
                "bone_01DB": "Back Flap 2 9",
                "bone_020D": "Back Flap 2 10",
                "bone_0214": "Back Flap 2 11",
                "bone_021B": "Back Flap 2 12",
                "bone_0222": "Back Flap 2 13",
                "bone_01EE": "Back Flap 3 1",
                "bone_01FE": "Back Flap 3 2",
                "bone_0257": "Back Flap 3 3",
                "bone_01F7": "Back Flap 3 4",
                "bone_0256": "Back Flap 3 5",
                "bone_01FA": "Back Flap 3 6",
                "bone_0253": "Back Flap 3 7",
                "bone_01FD": "Back Flap 3 8",
                "bone_01ED": "Back Flap 3 9",
                "bone_0213": "Back Flap 3 10",
                "bone_021A": "Back Flap 3 11",
                "bone_0221": "Back Flap 3 12",
                "bone_0228": "Back Flap 3 13",
                "bone_01F0": "Back Flap 4 1",
                "bone_024E": "Back Flap 4 2",
                "bone_01F1": "Back Flap 4 3",
                "bone_01F5": "Back Flap 4 4",
                "bone_0254": "Back Flap 4 5",
                "bone_01F8": "Back Flap 4 6",
                "bone_0251": "Back Flap 4 7",
                "bone_01FB": "Back Flap 4 8",
                "bone_0250": "Back Flap 4 9",
                "bone_0211": "Back Flap 4 10",
                "bone_0218": "Back Flap 4 11",
                "bone_021F": "Back Flap 4 12",
                "bone_0226": "Back Flap 4 13",
            },
        ),
    },
}
