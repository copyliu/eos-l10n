#Used by:
#Modules from group: Armor Repair Projector (37 of 37)
#Modules from group: Capacitor Booster (54 of 54)
#Modules from group: Energy Destabilizer (41 of 41)
#Modules from group: Energy Transfer Array (37 of 37)
#Modules from group: Energy Vampire (52 of 52)
#Modules from group: Hull Repair Unit (21 of 21)
#Modules from group: Shield Transporter (38 of 38)
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("duration", module.getModifiedItemAttr("overloadSelfDurationBonus"))