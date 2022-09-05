from typing import Dict, Optional

from owm_additions.bones.bone_group_mapping import BoneGroupMapping
from owm_additions.bones.heroes.mercy.all import MERCY_MAPPING
from owm_additions.bones.heroes.pharah.all import PHARAH_MAPPING

BASE_BONE_GROUP_MAPPINGS: Dict[str, BoneGroupMapping] = {
    "Body Pose": BoneGroupMapping(
        layers=[0],
        bones={
            "bone_0003": "Torso Upper",
            "bone_0004": "Waist",
            "bone_0005": "Chest",
            "bone_000D": "Shoulder L",
            "bone_000E": "Elbow L",
            "bone_0010": "Neck Lower",
            "bone_0011": "Neck Upper",
            "bone_0035": "Clavicle R",
            "bone_0036": "Shoulder R",
            "bone_0037": "Elbow R",
            "bone_0050": "Clavicle L",
            "bone_0053": "Torso Lower",
            "bone_0055": "Hip L",
            "bone_0059": "Leg L",
            "bone_005A": "Foot L",
            "bone_005F": "Hip R",
            "bone_0063": "Leg R",
            "bone_0064": "Foot R",
        },
    ),
    "Body Adjustments": BoneGroupMapping(
        layers=[1],
        bones={
            "bone_000C": "Clavicle Adjustment R",
            "bone_000F": "Chest Adjustment",
            "bone_001A": "Elbow Lower Adjustment L",
            "bone_001B": "Arm Lower Adjustment L",
            "bone_0030": "Wrist Adjustment L",
            "bone_0031": "Shoulder Adjustment L",
            "bone_0032": "Arm Upper Adjustment L",
            "bone_0033": "Elbow Upper Adjustment R",
            "bone_0034": "Clavicle Adjustment L",
            "bone_0038": "Elbow Lower Adjustmenr R",
            "bone_0039": "Arm Lower Adjustment R",
            "bone_004C": "Wrist Adjustment R",
            "bone_004D": "Shoulder Adjustment R",
            "bone_004E": "Arm Upper Adjustment R",
            "bone_004F": "Elbow Upper Adjustment L",
            "bone_0051": "Waist Upper Adjustment",
            "bone_0052": "Torso Upper Adjustment",
            "bone_0054": "Waist Lower Adjustment",
            "bone_0056": "Hip Adjustment L",
            "bone_0057": "Thigh Adjustment L",
            "bone_0058": "Knee Upper Adjustment L",
            "bone_005B": "Toes L",
            "bone_005C": "Knee Lower Adjustment L",
            "bone_005D": "Leg Adjustment L",
            "bone_005E": "Ankle Adjustment L",
            "bone_0060": "Hip Adjustment R",
            "bone_0061": "Thigh Adjustment R",
            "bone_0062": "Knee Upper Adjustment R",
            "bone_0065": "Toes R",
            "bone_0066": "Knee Lower Adjustment R",
            "bone_0067": "Leg Adjustment R",
            "bone_0068": "Ankle Adjustment R",
        },
    ),
    "Hands": BoneGroupMapping(
        layers=[2],
        bones={
            "bone_001C": "Wrist L",
            "bone_001D": "Index Inner L",
            "bone_001E": "Index Middle L",
            "bone_001F": "Index Outer L",
            "bone_0020": "Middle Inner L",
            "bone_0021": "Middle Middle L",
            "bone_0022": "Middle Outer L",
            "bone_0023": "Pinky Inner L",
            "bone_0024": "Pinky Middle L",
            "bone_0025": "Pinky Outer L",
            "bone_0026": "Ring Inner L",
            "bone_0027": "Ring Middle L",
            "bone_0028": "Ring Middle Outer",
            "bone_0029": "Thumb Inner L",
            "bone_002A": "Thumb Middle L",
            "bone_002B": "Thumb Outer L",
            "bone_003A": "Wrist R",
            "bone_003B": "Index Inner R",
            "bone_003C": "Index Middle R",
            "bone_003D": "Index Outer R",
            "bone_003E": "Middle Inner R",
            "bone_003F": "Middle Middle R",
            "bone_0040": "Middle Outer R",
            "bone_0041": "Pinky Inner R",
            "bone_0042": "Pinky Middle R",
            "bone_0043": "Pinky Outer R",
            "bone_0044": "Ring Inner R",
            "bone_0045": "Ring Middle R",
            "bone_0046": "Ring Outer R",
            "bone_0047": "Thumb Inner R",
            "bone_0048": "Thumb Middle R",
            "bone_0049": "Thumb Outer R",
        },
    ),
    "Face": BoneGroupMapping(
        layers=[16],
        bones={
            "bone_0008": "Nose",
            "bone_0009": "Nose L",
            "bone_000A": "Nose R",
            "bone_000B": "Face",
            "bone_0013": "Eyelash R 2",
            "bone_0014": "Eyelash R 1",
            "bone_0015": "Eyelash R 0",
            "bone_0016": "Forehead",
            "bone_0017": "Eyelash L 0",
            "bone_0018": "Eyelash L 1",
            "bone_0019": "Eyelash L 2",
            "bone_0384": "Eyelash R 3",
            "bone_0385": "Eyelash L 3",
            "bone_0388": "bone_0388",
            "bone_0389": "bone_0389",
            "bone_0396": "bone_0396",
            "bone_0397": "bone_0397",
            "bone_0398": "bone_0398",
            "bone_0399": "bone_0399",
            "bone_039E": "bone_039E",
            "bone_039F": "bone_039F",
            "bone_03A0": "bone_03A0",
            "bone_03A1": "bone_03A1",
            "bone_03A2": "bone_03A2",
            "bone_03A3": "bone_03A3",
            "bone_03A4": "bone_03A4",
            "bone_03A5": "bone_03A5",
            "bone_03A6": "bone_03A6",
            "bone_03A7": "bone_03A7",
            "bone_03A8": "bone_03A8",
            "bone_03A9": "bone_03A9",
            "bone_03AA": "bone_03AA",
            "bone_03AB": "bone_03AB",
            "bone_03AC": "bone_03AC",
            "bone_03AD": "bone_03AD",
            "bone_03AE": "bone_03AE",
            "bone_03AF": "bone_03AF",
            "bone_03B0": "bone_03B0",
            "bone_03B1": "bone_03B1",
            "bone_03B2": "bone_03B2",
            "bone_03B3": "bone_03B3",
            "bone_03B4": "bone_03B4",
            "bone_03B5": "bone_03B5",
            "bone_03B6": "bone_03B6",
            "bone_03B7": "bone_03B7",
            "bone_03B8": "bone_03B8",
            "bone_03B9": "bone_03B9",
            "bone_03BA": "bone_03BA",
            "bone_03BB": "bone_03BB",
            "bone_03BC": "Jaw",
            "bone_0608": "bone_0608",
            "bone_0609": "bone_0609",
            "bone_060A": "bone_060A",
            "bone_060B": "bone_060B",
            "bone_060C": "bone_060C",
            "bone_060D": "bone_060D",
            "bone_071D": "bone_071D",
            "bone_071E": "bone_071E",
        },
    ),
    "Eyelids": BoneGroupMapping(
        layers=[17],
        bones={
            "bone_0006": "bone_0006",
            "bone_0007": "bone_0007",
            "bone_0386": "bone_0386",
            "bone_0387": "bone_0387",
            "bone_038A": "bone_038A",
            "bone_038B": "bone_038B",
            "bone_038C": "bone_038C",
            "bone_038D": "bone_038D",
            "bone_038E": "bone_038E",
            "bone_038F": "bone_038F",
            "bone_0390": "bone_0390",
            "bone_0391": "bone_0391",
            "bone_0392": "bone_0392",
            "bone_0393": "bone_0393",
            "bone_0394": "bone_0394",
            "bone_0395": "bone_0395",
        },
    ),
    "Eyes": BoneGroupMapping(
        layers=[18], bones={"bone_039A": "bone_039A", "bone_039B": "bone_039B"}
    ),
    "Sockets": BoneGroupMapping(
        layers=[23],
        bones={
            "bone_0000": "Root",
            "bone_0001": "Ground",
            "bone_0002": "Body Root",
            "bone_002C": "Hand Socket L 1",
            "bone_002D": "Hand Socket L 2",
            "bone_002E": "Hand Socket L 3",
            "bone_004A": "Hand Socket R 1",
            "bone_007D": "Head Anchor",
            "bone_00C1": "Foot Anchor L",
            "bone_00C2": "Foot Anchor R",
            "bone_011C": "Hand Socket L 0",
            "bone_011D": "Hand Socket R 0",
            "bone_0164": "bone_0164",
            "bone_0165": "bone_0165",
            "bone_0166": "bone_0166",
            "bone_0167": "bone_0167",
            "bone_0180": "Hand Anchor L",
            "bone_0181": "Hand Anchor R",
            "bone_03BD": "Shoulder Anchor L",
            "bone_03BE": "Shoulder Anchor R",
            "bone_05F0": "Hair Anchor",
        },
    ),
}

SKIN_SPECIFIC_GROUPS: Dict[str, Dict[str, Dict[str, BoneGroupMapping]]] = (
    MERCY_MAPPING | PHARAH_MAPPING
)


def get_hero_base_bone_mapping(
    character: Optional[str] = None,
) -> Dict[str, Dict[str, BoneGroupMapping]]:
    character_mapping = SKIN_SPECIFIC_GROUPS.get(character, {})
    skin_mapping = character_mapping.get("Base", {})

    return skin_mapping


def get_skin_bone_mapping(
    character: Optional[str] = None, skin: Optional[str] = None
) -> Dict[str, Dict[str, BoneGroupMapping]]:
    character_mapping = SKIN_SPECIFIC_GROUPS.get(character, {})
    skin_mapping = character_mapping.get(skin, {})

    if len(character_mapping) == 0:
        print(f"Mapping for character `{character}` not found. Using default.")

    if len(skin_mapping) == 0:
        print(f"Mapping for skin `{skin}` not found. Using default.")

    return skin_mapping
