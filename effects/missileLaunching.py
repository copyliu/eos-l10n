#Used by: All missiles
from model import attribute
runTime = "late"
def missileLaunching(self, fitting, containerModule):
    #Set maxrange value for missiles here, as it's not available anywhere and this effect
    #is shared between all missiles
    flightTime = self.item.getModifiedAttribute("explosionDelay") / 1000.0
    speed = self.item.getModifiedAttribute("maxVelocity")
    containerModule.attributes["_maxMissileRange"] = attribute.basicAttribute(containerModule, "_maxMissileRange", None, flightTime * speed)
