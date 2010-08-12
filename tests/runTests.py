#===============================================================================
# This file is part of eos.
#
# eos is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# eos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with eos.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

import hashlib, unittest, os, os.path, sys

#Add the good path to sys.path
path = os.path.dirname(unicode(__file__, sys.getfilesystemencoding()))
sys.path.append(os.path.realpath(os.path.join(path, "..", "..")))

from eos import config

config.debug = False
config.saveddata_connectionstring = "sqlite:///:memory:"

suite = unittest.TestSuite()
loader = unittest.defaultTestLoader

def iteratedir(dir, prefix = []):
    for filename in os.listdir(dir or '.'):
        if os.path.isdir(os.path.join(dir, filename)):
            iteratedir(os.path.join(dir, filename), prefix + [filename])
        moduleName, ext = os.path.splitext(filename)
        if ext == ".py" and moduleName != "__init__":
            moduleName = '.'.join(prefix + [moduleName])
            module = __import__(moduleName, fromlist = True)
            suite.addTest(loader.loadTestsFromModule(module))

iteratedir(os.path.dirname(__file__))

if __name__ == "__main__":

    unittest.TextTestRunner().run(suite)
