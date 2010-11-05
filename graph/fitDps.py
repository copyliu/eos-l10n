from eos.graph import Graph, Data
from eos.types import Hardpoint

class FitDpsGraph(Graph):
    defaults = (Data("transversal", 0),
                Data("distance", 1),
                Data("signatureRadius", None))

    def __init__(self, fit, data=None):
        Graph.__init__(self, fit, self.calcDps, data if data is not None else self.defaults)
        self.fit = fit

    def calcDps(self, data):
        fit = self.fit

        total = 0
        for mod in fit.modules:
            if mod.hardpoint == Hardpoint.TURRET:
                totalDmg = 0
                for type in ("em", "kinetic", "explosive", "thermal"):
                    totalDmg += mod.getModifiedChargeAttr("%sDamage" % type)

                total += totalDmg * mod.getModifiedItemAttr("damageMultiplier") * self.calculateChanceToHit(mod, data) / mod.cycleTime

        return total * 1.03

    def calculateChanceToHit(self, mod, data):
        if mod.hardpoint != Hardpoint.TURRET:
            return 0

        distance = data["distance"]
        tracking = mod.getModifiedItemAttr("trackingSpeed")
        turretOptimal = mod.maxRange
        turretFalloff = mod.falloff
        turretSigRes = mod.getModifiedItemAttr("optimalSigRadius")
        targetSigRad = data["signatureRadius"]
        targetSigRad = turretSigRes if targetSigRad is None else targetSigRad

        trackingEq = (((data["transversal"] / (distance * tracking)) *
                       (turretSigRes / targetSigRad)) ** 2)
        rangeEq = ((max(0, distance - turretOptimal)) / turretFalloff) ** 2

        return 0.5 ** (trackingEq + rangeEq)
