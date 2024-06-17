
import re

letras_posibles="TRWAGMYFPDXBNJZSQVHLCKE"

class DNI:

    def __init__(self, dni_como_texto):
        self.dni_como_texto = self.pretratamiento_de_dni(dni_como_texto)

        self.confianza = 0
        (valido, numero, letra) = self.validar_dni(self.dni_como_texto)
        if(valido):
            self.confianza = 1
        else:
            (valido, numero, letra) = self.tratar_de_arreglar_el_dni()
            if(valido):
                self.confianza = 0.5
        self.valido = valido
        self.letra = letra
        self.numero = numero

    def letra_correspondiente(self,numero_dni):
        return letras_posibles[numero_dni % 23]

    def validar_dni(self, dni_como_texto):
        """                             VALIDACION                    -->   FORMATEO
        Me llegará algo como:       NUMERO          LETRA     VALIDO
            12345678T           ->  12345678        T           √           --> 12345678-T | 12345678T | 12345678 T | 12.345.678-T
            12345.678-T             12345678        T           x
            12.345.678 T            12345678        T           √
            00001234T               1234            T           x
            1234t                   1234            T           x
        """
        numero = None
        letra = None
        # Aplico una expresion regular
        valido = re.match(r'^[0-9]{1,8}[ -]?[a-zA-Z]$', dni_como_texto)
        if(valido):
            valido = True
            # Extraer la letra 
            letra = self.dni_como_texto[-1].upper()
            # Extraer el número
            dni_como_texto = dni_como_texto.replace(". -","") # Me como los espacios, puntos y guiones
            numero = int(dni_como_texto[:-1])
            # Validar la letra
            if self.letra_correspondiente(numero) != letra:
                valido = False
        else:
            valido = False
        return (valido, numero, letra)

    def tratar_de_arreglar_el_dni(self):
        """
            Si me vienen puntos en mal sitio, lo ignoro...                          [^a-zA-Z0-9]
            Si me viene algun caracter que no sea letras o numeros... los ignoro
        """
        dni_como_texto = re.sub(r'[^a-zA-Z0-9]','',self.dni_como_texto)
        print(dni_como_texto)
        return self.validar_dni(dni_como_texto)

    def pretratamiento_de_dni(self,dni_como_texto):
        return dni_como_texto.strip()
    
    def otra_funcion(self, loquesea):
        print(loquesea)
