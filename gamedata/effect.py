from sqlalchemy.orm import reconstructor

#Filter to change names of effects to valid python method names
nameFilter = dict((ord(char), '') for char in u'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')

class Effect(object):
    @reconstructor
    def init(self):
        self.__generated = False
        self.handlerName = self.name.translate(nameFilter)
        
    @property
    def handler(self):
        if not self.__generated: self.__generateHandler()
        return self.__handler
    
    @property
    def runTime(self):
        if not self.__generated: self.__generateHandler()
        return self.__runTime
    
    @property
    def type(self):
        if not self.__generated: self.__generateHandler()
        return self.__type
    
    def isType(self, type):
        return self.type != None and type in self.type
    
    def __generateHandler(self):
        try:
            effectModule = __import__('model.effects.' + self.name, fromlist=True)
            self.__handler = getattr(effectModule, "handler")
            try:
                self.__runTime = getattr(effectModule, "runTime")
            except AttributeError:
                self.__runTime = None
                
            try:
                t = getattr(effectModule, "type")
            except AttributeError:
                t = None
                
            t = t if isinstance(t, tuple) or t == None else (t,)
            self.__type = t
        except ImportError:
            self.__handler = effectDummy
            self.__runTime = None
            self.__type = None
        
        self.__generated = True


def effectDummy(*args, **kwargs):
    pass