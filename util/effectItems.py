import sqlite3
import sys
conn = sqlite3.connect('/home/cncfanatics/eve.db')
c = conn.cursor()
c.execute("SELECT it.typeName FROM invTypes it INNER JOIN dgmtypeeffects dte ON dte.typeID = it.typeID INNER JOIN dgmeffects de ON de.effectID = dte.effectID WHERE de.effectName = ?", (sys.argv[1],))
for row in c:
    print row[0]
