from typing import Literal

T_ParticleColorBlack = Literal["B"]
T_ParticleColorIndigo = Literal["I"]
T_ParticleColorLavender = Literal["L"]
T_ParticleColorTeal = Literal["T"]
T_ParticleColorCocoa = Literal["C"]
T_ParticleColorDark = Literal["D"]
T_ParticleColorOatmeal = Literal["O"]
T_ParticleColorWhite = Literal["W"]
T_ParticleColorRed = Literal["R"]
T_ParticleColorApricot = Literal["A"]
T_ParticleColorYellow = Literal["Y"]
T_ParticleColorGreen = Literal["G"]
T_ParticleColorVatblue = Literal["V"]
T_ParticleColorSlate = Literal["S"]
T_ParticleColorPink = Literal["P"]
T_ParticleColorFawn = Literal["F"]
T_ParticleColor = (
    T_ParticleColorBlack
    | T_ParticleColorIndigo
    | T_ParticleColorLavender
    | T_ParticleColorTeal
    | T_ParticleColorCocoa
    | T_ParticleColorDark
    | T_ParticleColorOatmeal
    | T_ParticleColorWhite
    | T_ParticleColorRed
    | T_ParticleColorApricot
    | T_ParticleColorYellow
    | T_ParticleColorGreen
    | T_ParticleColorVatblue
    | T_ParticleColorSlate
    | T_ParticleColorPink
    | T_ParticleColorFawn
)

T_PosDirection_NEG_Y = Literal[0]
T_PosDirection_POS_Y = Literal[1]
T_PosDirection_NEG_Z = Literal[2]
T_PosDirection_POS_Z = Literal[3]
T_PosDirection_NEG_X = Literal[4]
T_PosDirection_POS_X = Literal[5]
T_PosDirection = (
    T_PosDirection_NEG_X
    | T_PosDirection_NEG_Y
    | T_PosDirection_NEG_Z
    | T_PosDirection_POS_X
    | T_PosDirection_POS_Y
    | T_PosDirection_POS_Z
)

T_ParticleSize = Literal[1, 2, 4, 8, 16]
# fmt: off
T_ParticleNumber = Literal[
    0, 1, 2, 3, 4, 5, 6, 7, 8,
    9, 10, 11, 12, 13, 14, 15, 16,
    "0", "1", "2", "3", "4", "5", "6", "7", "8",
    "9", "10", "11", "12", "13", "14", "15", "16",
    "A", "B", "C", "D", "E", "F",
]
# fmt: on
