import itertools

class Graph(object):
    def __init__(self, fit, function, data = tuple()):
        self.fit = fit
        self.data = {}
        for d in data:
            self.setData(d)

        self.function = function

    def setData(self, data):
        self.data[data.name] = data

    def getIterator(self):
        pointNames = []
        pointIterators = []
        for data in self.data.itervalues():
                pointNames.append(data.name)
                pointIterators.append(data)

        return pointNames, self._iterator(pointNames, pointIterators)

    def _iterator(self, pointNames, pointIterators):
        for pointValues in itertools.product(*pointIterators):
            point = {}
            for i in xrange(len(pointValues)):
                point[pointNames[i]] = pointValues[i]

            yield point, self.function(point)


class Data(object):
    def __init__(self, name, dataString, step=1):
        self.name = name
        self.step = step
        self.data = self.parseString(dataString)

    def parseString(self, dataString):
        if not isinstance(dataString, basestring):
            return (Constant(dataString),)

        dataList = []
        for data in dataString.split(";"):
            if isinstance(data, basestring) and "-" in data:
                #Dealing with a range
                dataList.append(Range(data, self.step))
            else:
                dataList.append(Constant(data))

        return dataList

    def __iter__(self):
        for data in self.data:
            for value in data:
                yield value

    def isConstant(self):
        return len(self.data) == 1 and self.data[0].isConstant()


class Constant(object):
    def __init__(self, const):
        if isinstance(const, basestring):
            self.value = float(const)
        else:
            self.value = const

    def __iter__(self):
        yield self.value

    def isConstant(self):
        return True

class Range(object):
    def __init__(self, string, step):
        start, end = string.split("-")
        self.start = float(start)
        self.end = float(end)
        self.step = step

    def __iter__(self):
        current = start = self.start
        end = self.end
        step = self.step
        i = 1
        while current < end:
            current = start * i * step
            i += 1
            yield current

    def isConstant(self):
        return False
