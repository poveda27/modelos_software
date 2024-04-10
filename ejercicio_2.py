

class Motor:  
    """This class represents the behaviour of a vehicle motor"""

    def __init__(
        self, nob_motor: str, tipo_motor: str, pontecion_motor: int, peso: float
    ):
        self.__nombre = nob_motor
        self.__tipo = tipo_motor
        self.__pontencial = pontecion_motor
        self.__peso = peso

    def get_potency(self) -> int:
        """
        This method returns the potency of the engine.

        Returns:
        - int: potency of the engine
        """
        return self.__pontencial

    def get_weight(self) -> int:
        """
        This method returns the weight of the engine.

        Returns:
        - int: weight of the engine
        """
        return self.__weight

    def __str__(self):
        return f"Name: {self.__nombre}    Type: {self.__tipo}    \
            Potency: {self.__pontencial}    Weight: {self.__peso}"
class Vehiculos():
    """ la clase es la creaacion del los vehiculos"""
    def __init__(self,motor:Motor,chasis: str,modelo:str,año:int, marca:str,transmicion:str):
        self.motor=motor
        self.chasis=chasis
        self.modelo=modelo
        self.año=año
        self.marca=marca
        self.transmicion=transmicion
        self.consumo= self.__calculate_gas_consupmtion()
    def __calculate_gas_consupmtion(self) -> float:
        """
        This method calculates consumption based on engine
        values.

        Returns:
        - float: vehicle consumption
        """
        consumption = (
            (1.1 * self.__motor.get_potency())
            + (0.2 * self.__engine.weight)
            + (0.3 if self.__chasis == "A" else 0.5)
        )
    def crear_vehiculo(self,tipo_vehiculo: str):
        """
        This method lets create a new vehicle and add it to the
        catalog.

        Parameters:
         - type_vehicle (str): The type of the vehicle
        """
        vehiculos=[]
        chassis = input("Write the chassis of the vehicle (A or B):")
        marca = input("escribir la marca del vehiculo:")
        if chassis not in ["A", "B"]:
           raise ValueError("Error: Chassis wrote is wrong. Must be A or B.")
        self.modelo = input("Write the model of the vehicle: ")
        self.año = int(
            input("Write the year of the vehicle (should be greater or equal than 2000): ")
        )
        if self.año < 2000:
            raise ValueError("Error. Year is not in a valid range.")
        try:
            if tipo_vehiculo == "carro":
               vehicle_obj_new = Car(self.motor, chassis, self.modelo, self.año)
            elif tipo_vehiculo == "camion":
               vehicle_obj_new = Truck(self.motor, chassis, self.modelo, self.año)
            elif tipo_vehiculo == "yate":
               vehicle_obj_new = Yatch(self.motor, chassis, self.modelo, self.año)
            elif tipo_vehiculo == "motocicletae":
               vehicle_obj_new = Motorcycle(self.motor, chassis, self.modelo, self.año)
            elif tipo_vehiculo == "helicoptero":
                vehicle_obj_new = So(self.motor, chassis, self.modelo, self.año)
            vehiculos.append(vehicle_obj_new)
        except Exception as e:
            print(f"Error: {e}.")
class Car(Vehiculos):  # pylint: disable=too-few-public-methods
    """This class represents the behevior of a Car vehicle"""


class Truck(Vehiculos):  # pylint: disable=too-few-public-methods
    """This class represents the behavior of a Truck vehicle"""


class Yatch(Vehiculos):  # pylint: disable=too-few-public-methods
    """This class represents the behavior of a Yatch vehicle"""


class Motorcycle(Vehiculos):  # pylint: disable=too-few-public-methods
    """This class represents the behavior of a Motorcycle vehicle"""

class Hepcopter(Vehiculos):  # pylint: disable=too-few-public-methods
    """This class represents the behavior of a hepcopter vehicle"""
class So(Vehiculos):  # pylint: disable=too-few-public-methods
    """This class represents the behavior of a hepcopter vehicle"""
# ==================================== MENU
vehiculos=Vehiculos()
MESSAGE = """
Opción 1. crear motor
Opción 1. crear carro
Opción 2. crear camion
Opción 3. crear yate
Opción 4. Crear motocicleta
Opción 5. Crear helecotero
Opción 6. Crear scooter

Opción 11. Salir
"""

motores = {}
vehículos = Vehiculos()
print(MESSAGE)
option = int(input("Por favor, elige una opción: "))
while option != 11:
    
    if option == 1:
        vehiculos.crear_vehiculo("carro")
    elif option == 2:
        vehiculos.crear_vehiculo("camion")
    elif option == 4:
        vehiculos.crear_vehiculo("yate")
    elif option == 5:
        vehiculos.crear_vehiculo("motocicleta")
    elif option == 6:
        vehiculos.crear_vehiculo("helecotero")
    elif option == 7:
        vehiculos.crear_vehiculo("scooter")
    elif option == 8:
        """"""
    elif option == 9:
        """"""
    elif option == 10:
        """"""
    elif option == 11:
        """"""
    else:
        print("Invalid option.")
    print("\n\n" + MESSAGE)
    option = int(input("Please, choise an option: "))