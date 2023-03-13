class StatSheet():
    def __init__(self):
        self.money = 0
        self.dirt = 0
    
    @property
    def money(self):
        return self._money
    
    @money.setter
    def money(self, val):
        if val <= 0:
            self._money = 0
        else:
            self._money = val
    
    @property
    def dirt(self):
        return self._dirt
    
    @dirt.setter
    def dirt(self, val):
        if val <= 0:
            self._dirt = 0
        else:
            self._dirt = val