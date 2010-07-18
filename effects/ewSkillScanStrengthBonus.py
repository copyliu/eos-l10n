#Variations of item: Large Particle Dispersion Augmentor I (2 of 2)
#Variations of item: Medium Particle Dispersion Augmentor I (2 of 2)
#Variations of item: Small Particle Dispersion Augmentor I (2 of 2)
#Item: Signal Dispersion
from customEffects import boostModListByReq
def ewSkillScanStrengthBonus(self, fitting, level = 1, state = None):
    for scanType in ("Gravimetric", "Radar", "Ladar", "Magnetometric"):
        boostModListByReq(fitting.modules, "scan" + scanType + "StrengthBonus", "scanSkillEwStrengthBonus",
                          lambda mod: mod.group.name == "ECM" or mod.group.name == "ECM Burst",
                          self.item, extraMult = level)