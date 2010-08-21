def cachedQuery(function):
    cache = {}
    def checkAndReturn(*args, **kwargs):
        if args[0] not in cache:
            cache[args[0]] = function(*args, **kwargs)

        return cache[args[0]]

    return checkAndReturn
