class Item(object):
    def getAttribute(self, key):
        if key in self.attributes:
            return self.attributes[key].value