if __name__ == "__main__":
    print "starting"
    import os
    import sys
    import os.path

    #Add the good path to sys.path
    path = os.path.realpath(os.path.join(sys.path[0], "..", ".."))
    sys.path.append(path)

    from model.types import Effect
    from model.gamedata import effectDummy

    print "checking files in effects folder"
    list = os.listdir(os.path.join("../effects"))
    def validate(fileName):
        moduleName, ext = os.path.splitext(fileName)
        return moduleName != "__init__" and ext == ".py"

    list = filter(validate, list)
    size = len(list)
    print "found %d effects, starting checks:" % size
    i = 0
    lastError = -500
    errors = 0
    errorString = ""
    for fileName in list:
        moduleName, ext = os.path.splitext(fileName)
        i += 1
        if i / 50.0 == int(i / 50.0):
            sys.stdout.write(".")

        e = Effect()
        e.name = unicode(moduleName)
        try:
            e.init()

            if e.handler == effectDummy:
                errors += 1
                sys.stdout.write("F")
                errorString += "\n%s: No handler" % moduleName
            if e.type == None:
                errors += 1
                sys.stdout.write("F")
                errorString += "\n%s: No type" % moduleName
        except Exception, exc:
            errors += 1
            sys.stdout.write("E")
            errorString += "\n%s: Exception thrown: %s\n%s\n" % (moduleName, exc.__class__, exc)

    sys.stderr.write(errorString)

    print ""
    print "Done"
    print "%d errors with a total of %d effects (%.2f%%)" % (errors, size, float(errors) / size * 100)
