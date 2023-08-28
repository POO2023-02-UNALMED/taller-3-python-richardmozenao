class TV:
    numTV = 0

    @classmethod
    def nuevoTV(cls):
        cls.numTV += 1

    @classmethod
    def setNumTV(cls, p):
        cls.NumTV = p

    @classmethod
    def getNumTV(cls):
        return cls.numTV

    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control = None
        TV.nuevoTV()

    def getControl(self):
        return self._Control

    def setControl(self, p):
        self._Control = p

    def getMarca(self):
        return self._marca

    def setMarca(self, p):
        self._marca = p

    def getEstado(self):
        return self._estado

    def setEstado(self, p):
        self._estado = p

    def getCanal(self):
        return self._canal

    def setCanal(self, p):
        if 1 <= p <= 120 and self._estado == True:
            self._canal = p

    def getVolumen(self):
        return self._volumen

    def setVolumen(self, p):
        if 0 <= p <= 7 and self._estado == True:
            self._volumen = p

    def getPrecio(self):
        return self._precio

    def setPrecio(self, p):
        self._precio = p

    def turnOn(self):
        self.setEstado(True)

    def turnOff(self):
        self.setEstado(False)

    def volumenUp(self):
        self.setVolumen(self.getVolumen()+1)

    def volumenDown(self):
        self.setVolumen(self.getVolumen()-1)

    def canalUp(self):
        self.setCanal(self.getCanal()+1)

    def canalDown(self):
        self.setCanal(self.getCanal()-1)
