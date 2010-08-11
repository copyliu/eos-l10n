def cachedQuery(function):
    cache = {}
    def checkAndReturn(*args):
        if args not in cache:
            cache[args] = function(*args)

        return cache[args]

    return checkAndReturn
