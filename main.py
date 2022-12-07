"""ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’
"""
from abc import ABC, abstractmethod
class FormaGeometrica(ABC):
    PI = 3.14
    @abstractmethod
    def aria(self):
        pass
    def descrie(cls):
        print('cel mai probabil am colturi')
forma=FormaGeometrica()

"""
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură
ENCAPSULATION
latura este proprietate privată"""
"""Implementează getter, setter, deleter pentru latură"""

"""
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)- cum adica ??????????
"""

class Patrat(FormaGeometrica):
    def __init__(self,latura):
        self.__latura=latura

    @getter
    def getter(self):
        print(f"Latura este {self.__latura}")
        return self.__latura

    @setter
    def setter(self,noua_latura):
        self.__latura=noua_latura

    @deleter
    def deleter(self):
        self.__latura=None
        print("Am sters latura")

    def aria(self):
        self.aria_patratului=self.__latura**2
        return self.aria_patratului


"""Clasa Cerc - moștenește FormaGeometrica constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază"""

class Cerc(FormaGeometrica):
    def __init__(self,raza):
        self.__raza=raza
    @getter
    def getter(self):
        print(f"Raza este {self.__raza}")
        return self.__raza
    @setter
    def setter(self,noua_raza):
        self.__raza=noua_raza
    @deleter
    def deleter(self):
        self.__raza=None
        print("Am sters raza")

    def aria(self):
        aria_cercului = self.PI * (self.__raza**2)
        return aria_cercului

"""Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)"""
