def cachedQuery(function):
    cache = {}
    def checkAndReturn(*args, **kwargs):
        if args not in cache:
            cache[args] = function(*args, **kwargs)

        return cache[args]

    return checkAndReturn
