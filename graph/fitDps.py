#===============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of eos.
#
# eos is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# eos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with eos.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

from eos.graph import Graph, Data
from eos.types import Hardpoint, State
from math import log

class FitDpsGraph(Graph):
    defaults = {"speed": 0,
                "transversal": 0,
                "distance": 1,
                "signatureRadius": None,
                "velocity": 0}

    def __init__(self, fit, data=None):
        Graph.__init__(self, fit, self.calcDps, data if data is not None else self.defaults)
        self.fit = fit

    def calcDps(self, data):
        fit = self.fit

        total = 0
        for mod in fit.modules:
            if mod.hardpoint == Hardpoint.TURRET:
                if mod.state >= State.ACTIVE:
                    total += mod.dps * self.calculateTurretMultiplier(mod, data)

            elif mod.hardpoint == Hardpoint.MISSILE:
                if mod.state >= State.ACTIVE and mod.maxRange >= data["distance"]:
                    total += mod.dps * self.calculateMissileMultiplier(mod, data)

        if data["distance"] <= fit.extraAttributes["droneControlRange"]:
            for drone in fit.drones:
                total += drone.dps * drone.amountActive

        return total

    def calculateMissileMultiplier(self, mod, data):
        targetSigRad = data["signatureRadius"]
        targetVelocity = data["velocity"]
        targetSigRad = turretSigRes if targetSigRad is None else targetSigRad
        explosionRadius = mod.getModifiedChargeAttr("aoeCloudSize")
        explosionVelocity = mod.getModifiedChargeAttr("aoeVelocity")
        damageReductionFactor = mod.getModifiedChargeAttr("aoeDamageReductionFactor")
        damageReductionSensitivity = mod.getModifiedChargeAttr("aoeDamageReductionSensitivity")

        sigRadiusFactor = targetSigRad / explosionRadius
        velocityFactor = (explosionVelocity / explosionRadius * targetSigRad / targetVelocity) ** (log(damageReductionFactor) / log(damageReductionSensitivity))
        return min(sigRadiusFactor , velocityFactor, 1)

    def calculateTurretMultiplier(self, mod, data):
        #Source for most of turret calculation info: http://wiki.eveonline.com/en/wiki/Falloff
        chanceToHit = self.calculateTurretChanceToHit(mod, data)
        if chanceToHit > 0.01:
            #AvgDPS = Base Damage * [ ( ChanceToHit^2 + ChanceToHit + 0.0499 ) / 2 ]
            return (chanceToHit ** 2 + chanceToHit + 0.0499) / 2
        else:
            #All hits are wreckings
            return chanceToHit * 3

    def calculateTurretChanceToHit(self, mod, data):
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