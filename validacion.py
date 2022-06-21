import re

class Validacion():
    def validarCorreo(self,cadena):
        self.__expresionReCorreos=r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"    
        if bool(re.match(self.__expresionReCorreos,cadena)):
            return True
        else:
            return False

    def validarEntero(self,cadena):
        self.__expreionNumeros=r"^[-+]?\d+$"
        if bool(re.match(self.__expreionNumeros,cadena)):
            return True
        else:
            return False

    def validarReal(self,cadena):
        self.__expresionNumerosR=r"^[+-]?\d+[.]\d+$"
        if bool(re.match(self.__expresionNumerosR,cadena)):
            return True
        else:
            return False

    def validarNotC(self,cadena):
        self.__expresionNotC=r"^[-+]?[0-9]+[.][0-9]+[eE]([-+])?[0-9]+"
        if bool(re.match(self.__expresionNotC,cadena)):
            return True
        else:
            return False