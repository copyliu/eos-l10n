#Used by: Item: Damage Control
import model.fitting
from customEffects import multiply
type = "active"
def damageControl(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        for layer, attrPrefix in (('shield', 'shield'), ('armor', 'armor'), ('hull', '')):
            for damageType in ('Kinetic', 'Thermal', 'Explosive', 'Em'):
                attrName = attrPrefix + damageType + 'DamageResonance'
                attrName = attrName[0].lower() + attrName[1:]
                multiply(fitting.ship, attrName, 
                      layer + damageType + 'DamageResonance', self.item)