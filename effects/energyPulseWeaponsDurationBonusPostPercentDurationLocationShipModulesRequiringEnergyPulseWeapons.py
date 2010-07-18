#Item: Energy Pulse Weapons [Skill]
#Item: Hardwiring - Inherent Implants 'Squire' EP2 [Implant]
#Item: Hardwiring - Inherent Implants 'Squire' EP4 [Implant]
#Item: Hardwiring - Inherent Implants 'Squire' EP8 [Implant]
from customEffects import boostModListByReq
def energyPulseWeaponsDurationBonusPostPercentDurationLocationShipModulesRequiringEnergyPulseWeapons(self, fitting, level = 1):
    boostModListByReq(fitting.modules, "duration", "durationBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)