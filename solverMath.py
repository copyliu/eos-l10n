#===============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of pyfa.
#
# pyfa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyfa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with pyfa.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

from math import pi, sqrt, exp

def gaussian(expected_value, variance):
  a = 1.0 / sqrt(2.0 * variance * pi)
  b = expected_value
  c = sqrt(variance)

  return lambda x: a * exp(-((x - b) ** 2) / (2 * c ** 2))


def solve(f_prime, initial_value, h = 0.2, max_iterations = 100):
  t, y = 0.0, initial_value
  try:
    for i in xrange(max_iterations):
      k_1 = f_prime(t, y)
      k_2 = f_prime(t + h / 2.0, y + h / 2.0 * k_1)
      k_3 = f_prime(t + h / 2.0, y + h / 2.0 * k_2)
      k_4 = f_prime(t + h, y + h * k_3)

      t, y = t + h, y + h / 6.0 * (k_1 + 2.0 * k_2 + 2.0 * k_3 + k_4)
  except ValueError:
    return t

  raise Exception("Didn't find a result")
