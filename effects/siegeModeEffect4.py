#Item: Siege Module I [Module]
from customEffects import boost, multiply, boostModListByReq, boostModListBySkillReq, boostAmmoListBySkillReq
import model.fitting
type = "active"
def siegeModeEffect4(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        #Turrets
        boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                          lambda skill: skill.name == "Gunnery",
                          self.item)
        boostModListBySkillReq(fitting.modules, "trackingSpeed", "trackingSpeedBonus",
                          lambda skill: skill.name == "Gunnery",
                          self.item)
        #Missiles
        for damageType in ("kinetic", "thermal", "explosive", "em"):
            boostAmmoListBySkillReq(fitting.modules, damageType + "Damage", "damageMultiplierBonus",
                                    lambda skill: skill.name == "Missile Launcher Operation",
                                    self.item)
        boostAmmoListBySkillReq(fitting.modules, "aoeVelocity", "aoeVelocityBonus",
                                lambda skill: skill.name == "Missile Launcher Operation",
                                self.item)
        #Shield booster
        boostModListByReq(fitting.modules, "duration", "shieldBonusDurationBonus",
                          lambda mod: mod.group.name == "Shield Booster",
                          self.item)
        boostModListByReq(fitting.modules, "shieldBonus", "shieldBoostMultiplier",
                          lambda mod: mod.group.name == "Shield Booster",
                          self.item)
        #Armor repper
        boostModListByReq(fitting.modules, "armorDamageAmount", "armorDamageAmountBonus",
                          lambda mod: mod.group.name == "Armor Repair Unit",
                          self.item)
        boostModListByReq(fitting.modules, "duration", "armorDamageDurationBonus",
                          lambda mod: mod.group.name == "Armor Repair Unit",
                          self.item)
        #Speed penalty
        boost(fitting.ship, "maxVelocity", "speedFactor", self.item)

        #Mass
        multiply(fitting.ship, "mass", "massMultiplier", self.item)

        #Scan resolution
        multiply(fitting.ship, "scanResolution", "scanResolutionMultiplier", self.item)
        
        #Max locked targets
        fitting.ship.attributes["maxLockedTargets"].overrideValue = self.item.getModifiedAttribute("maxLockedTargets")

        #Block Hostile EWAR and friendly effects
        fitting.ship.attributes["disallowOffensiveModifiers"] = self.item.attributes["disallowOffensiveModifiers"]
        fitting.ship.attributes["disallowAssistance"] = self.item.attributes["disallowAssistance"]
