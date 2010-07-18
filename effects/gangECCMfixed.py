#Item: Information Warfare Link - Sensor Integrity
from customEffects import boost
import model.fitting
type = ("gang", "active")

def gangECCMfixed(self, fitting, state):
    skill, level = fitting.getCharSkill("Information Warfare Specialist")
    if state >= model.fitting.STATE_ACTIVE:
        boost(
            fitting.ship,
            (
                "scanGravimetricStrength",
                "scanRadarStrength",
                "scanLadarStrength",
                "scanMagnetometricStrength",
            ),
            "commandBonus",
            self.item,
            useStackingPenalty = True
        )
