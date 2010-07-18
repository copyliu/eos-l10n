#Item: Triage Module I
import model.fitting
from customEffects import increase, multiply, boost, boostModListByReq, boostModListBySkillReq
type = "active"
def triageModeEffect2(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        #Remote armor rep
        boostModListBySkillReq(fitting.modules, "duration", "remoteArmorDamageDurationBonus",
                               lambda skill: skill.name == "Capital Remote Armor Repair Systems",
                               self.item)
        boostModListBySkillReq(fitting.modules, "armorDamageAmount", "remoteArmorDamageAmountBonus",
                               lambda skill: skill.name == "Capital Remote Armor Repair Systems",
                               self.item)
        #Remote mantank repairer
        boostModListBySkillReq(fitting.modules, "structureDamageAmount", "remoteHullDamageAmountBonus",
                               lambda skill: skill.name == "Capital Remote Hull Repair Systems",
                               self.item)
        boostModListBySkillReq(fitting.modules, "duration", "remoteHullDamageDurationBonus",
                               lambda skill: skill.name == "Capital Remote Hull Repair Systems",
                               self.item)
        
        #Shield transporter
        boostModListBySkillReq(fitting.modules, "duration", "shieldTransportDurationBonus",
                               lambda skill: skill.name == "Capital Shield Emission Systems",
                               self.item)
        boostModListBySkillReq(fitting.modules, "shieldBonus", "shieldTransportAmountBonus",
                               lambda skill: skill.name == "Capital Shield Emission Systems",
                               self.item)
        
        #Energy transfer array
        boostModListBySkillReq(fitting.modules, "powerTransferAmount", "powerTransferAmountBonus",
                               lambda skill: skill.name == "Capital Energy Emission Systems",
                               self.item)
        boostModListBySkillReq(fitting.modules, "duration", "powerTransferDurationBonus",
                               lambda skill: skill.name == "Capital Energy Emission Systems",
                               self.item)
        #Shield Booster
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

        #Speed bonus
        boost(fitting.ship, "maxVelocity", "speedFactor", self.item)

        #Mass
        multiply(fitting.ship, "mass", "massMultiplier", self.item)

        #Drone bonus
        boost(fitting.ship, "_maxActiveDrones", "maxDronePercentageBonus", self.item)

        #Max targets bonus
        increase(fitting.ship, "maxLockedTargets", "maxLockedTargetsBonus", self.item)
        
        #Block Hostile EWAR and friendly effects
        fitting.ship.attributes["disallowOffensiveModifiers"] = self.item.attributes["disallowOffensiveModifiers"]
        fitting.ship.attributes["disallowAssistance"] = self.item.attributes["disallowAssistance"]
