#Used by: Scorpion
from customEffects import boostModListByReq
def caldariShipEwStrengthCB(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Battleship")
    for sensorType in ("Gravimetric", "Ladar", "Magnetometric", "Radar"):
        boostModListByReq(fitting.modules, "scan" + sensorType + "StrengthBonus", "shipBonusCB",
                          lambda mod: mod.group.name == "ECM",
                          self.item, extraMult = level)
