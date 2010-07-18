#Item: 'Langour' Drive Disruptor I
#Item: Berserker SW-900
#Item: Caldari Navy Stasis Webifier
#Item: Civilian Stasis Webifier
#Item: Dark Blood Stasis Webifier
#Item: Domination Stasis Webifier
#Item: Dread Guristas Stasis Webifier
#Item: Federation Navy Stasis Webifier
#Item: Fleeting Propulsion Inhibitor I
#Item: Gotan's Modified Stasis Webifier
#Item: Hakim's Modified Stasis Webifier
#Item: Khanid Navy Stasis Webifier
#Item: Mizuro's Modified Stasis Webifier
#Item: Patterned Stasis Web I
#Item: Shadow Serpentis Stasis Webifier
#Item: Stasis Webifier I
#Item: Stasis Webifier II
#Item: Tobias' Modified Stasis Webifier
#Item: True Sansha Stasis Webifier
#Item: X5 Prototype I Engine Enervator
import model.fitting
from customEffects import boost
type = ("projected", "active")
def decreaseTargetSpeed(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE and fitting.ship.getModifiedAttribute("disallowOffensiveModifiers") != 1:
        boost(fitting.ship, "maxVelocity", "speedFactor", self.item, useStackingPenalty = True)
