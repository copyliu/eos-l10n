#Items from group: Shield Hardener (91 of 91) [Module]
from model.types import State          
type = "passive"
def handler(fit, module, context):
    if module.state != State.ONLINE: return
    for damageType in ("Kinetic", "Thermal", "Explosive", "Em"):
        if damageType == "Thermal":
            dn = "Thermic"
        else:
            dn = damageType
        fit.ship.boostItemAttr("shield%sDamageResonance" % damageType,
                               module.getModifiedItemAttr("passive%sDamageResistanceBonus" % dn),
                               stackingPenalties = True)