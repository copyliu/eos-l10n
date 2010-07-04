from sqlalchemy.orm import reconstructor

class Effect(object):
    nameFilter =''.join(c for c in map(chr,range(256)) if not c.isalnum())
    
    @reconstructor
    def init(self):
        self.__generated = False
        self.handlerName = self.name.translate(None, nameFilter)
        
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
    
    def __generateHandler(self):
        try:
            effectModule = __import__('model.effects.' + self.name, fromlist=True)
            self.__handler = getattr(effectModule, self.handlerName)
            self.__runTime = getattr(effectModule, "runTime")
            t = getattr(effectModule, "type")
            t =  t if t != None else "normal"
            t = t if type(t) == tuple else (t,)
            self.__type = t
        except ImportError:
            self.__handler = None
            self.__runTime = None
            self.__type = ("normal",)
            
        self.__generated = True