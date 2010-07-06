#Used by: Skill: Energy Pulse Weapons
from customEffects import boostModListByReq
def energyPulseWeaponsDurationBonusPostPercentDurationLocationShipModulesRequiringEnergyPulseWeapons(self, fitting, level = 1):
    boostModListByReq(fitting.modules, "duration", "durationBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)