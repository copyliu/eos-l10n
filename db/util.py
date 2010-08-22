def cachedQuery(amount, *keywords):
    cache = {}

    def deco(function):
        def checkAndReturn(*args, **kwargs):
            kw = []
            for keyword in keywords:
                if keyword in kwargs:
                    kw.append(kwargs[keyword])

            kw = tuple(kw)
            cacheKey = (args[0:amount], kw)
            if cacheKey not in cache:
                cache[cacheKey] = function(*args, **kwargs)

            return cache[cacheKey]

        return checkAndReturn

    return deco


def processEager(eager):
    if eager == None:
        return tuple()
    else:
        l = []
        if isinstance(eager, basestring):
            eager = (eager,)

        for e in eager:
            l.append(eagerload(e))

        return l
