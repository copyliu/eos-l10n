#Item: 'Langour' Drive Disruptor I [Module]
#Item: Berserker SW-900 [Drone]
#Item: Caldari Navy Stasis Webifier [Module]
#Item: Civilian Stasis Webifier [Module]
#Item: Dark Blood Stasis Webifier [Module]
#Item: Domination Stasis Webifier [Module]
#Item: Dread Guristas Stasis Webifier [Module]
#Item: Federation Navy Stasis Webifier [Module]
#Item: Fleeting Propulsion Inhibitor I [Module]
#Item: Gotan's Modified Stasis Webifier [Module]
#Item: Hakim's Modified Stasis Webifier [Module]
#Item: Khanid Navy Stasis Webifier [Module]
#Item: Mizuro's Modified Stasis Webifier [Module]
#Item: Patterned Stasis Web I [Module]
#Item: Shadow Serpentis Stasis Webifier [Module]
#Item: Stasis Webifier I [Module]
#Item: Stasis Webifier II [Module]
#Item: Tobias' Modified Stasis Webifier [Module]
#Item: True Sansha Stasis Webifier [Module]
#Item: X5 Prototype I Engine Enervator [Module]
import model.fitting
from customEffects import boost
type = ("projected", "active")
def decreaseTargetSpeed(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE and fitting.ship.getModifiedAttribute("disallowOffensiveModifiers") != 1:
        boost(fitting.ship, "maxVelocity", "speedFactor", self.item, useStackingPenalty = True)
