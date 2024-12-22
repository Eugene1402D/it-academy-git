import math
import random


class ArtilleryBrigade:
    """Создание класса артиллерийская бригада"""

    def __init__(self, call_sign: str, x: int = 0, y: int = 0, h: int = 0) -> None:
        """Инициализация объектов класса артиллерийская бригада"""
        self.call_sign = call_sign
        self.x = x
        self.y = y
        self.h = h


class CoordDescriptor:
    """Создание класса дескриптора для проверки данных ручного ввода"""

    @classmethod
    def verify_coord(cls, name: str, coord: int) -> None:
        """Метод проверки данных при ручном вводе координат"""
        if name in ["_x", "_y"] and len(str(coord)) < 5:
            raise ValueError(f"Координата {coord} должна быть не менее, чем 5 цифр.")
        if name == "_h" and len(str(coord)) != 3:
            raise ValueError(f"Высота {coord} должна быть в заданном диапазоне")

    def __set_name__(self, owner: type, name: str) -> None:
        self.name = "_" + name

    def __get__(self, instance: object, owner: type) -> int:
        return getattr(instance, self.name)

    def __set__(self, instance: object, value: int) -> None:
        self.verify_coord(self.name, value)
        setattr(instance, self.name, value)


class MovingUnits(ArtilleryBrigade):
    """Создание класса подразделений способных к перемещению"""

    x = CoordDescriptor()
    y = CoordDescriptor()
    h = CoordDescriptor()

    def move_to(self) -> [int, int, int]:
        """Метод ручного ввода координат для перемещения подразделений"""
        self.x = int(input("Введите координату х: "))
        self.y = int(input("Введите координату y: "))
        self.h = int(input("Введите высоту h: "))
        print(
            f"Прибыл в точку с координатами:"
            f"x: {self.x} y: {self.y} высота: {self.h}."
        )
        return self.x, self.y, self.h


class CoordinateGenerator:
    """Создание класса отвечающего за генерацию координат"""

    @staticmethod
    def generate_recon_coordinates() -> [int, int, int]:
        """Метод генерации координат подразделений разведки"""
        x = random.randint(15000, 19000)
        y = random.randint(58000, 60000)
        h = random.randint(150, 170)
        return x, y, h

    @staticmethod
    def generate_fire_coordinates() -> [int, int, int]:
        """Метод генерации координат огневых подразделений"""
        x = random.randint(19000, 23000)
        y = random.randint(63000, 66000)
        h = random.randint(150, 175)
        return x, y, h

    @staticmethod
    def generate_target_coordinates() -> [int, int, int]:
        """Метод генерации координат цели"""
        x = random.randint(18000, 21000)
        y = random.randint(45000, 56000)
        h = random.randint(150, 165)
        return x, y, h

    @staticmethod
    def generate_target_number() -> int:
        """Метод генерации номера цели"""
        targ_number = random.randint(100, 199)
        return targ_number


class ArtilleryReconnaissance(MovingUnits):
    """Создание класса подразделений артиллерийской разведки"""

    recon_range = 9000

    def __init__(self, call_sign: str, x: int, y: int, h: int) -> None:
        """Инициализация объектов класса подразделений артиллерийской разведки"""
        super().__init__(call_sign, x, y, h)
        # self.recon_range = recon_range
        print(f"Экземпляр класса '{self.call_sign}' создан.")

    @staticmethod
    def generate_coord() -> [int, int, int]:
        """Метод получения координат наблюдательного пункта"""
        return CoordinateGenerator.generate_recon_coordinates()

    @staticmethod
    def generate_target_coord() -> [int, int, int]:
        """Метод получения координат цели"""
        return CoordinateGenerator.generate_target_coordinates()

    @staticmethod
    def generate_target_number() -> int:
        """Метод получения номера цели"""
        return CoordinateGenerator.generate_target_number()


class FiringUnits(MovingUnits):
    """Создание класса огневых подразделений"""

    caliber = 152
    amount_ammunition = 360

    def __init__(self, call_sign: str, x: int, y: int, h: int, fire_range: int) -> None:
        """Инициализация объектов класса огневых подразделений"""
        super().__init__(call_sign, x, y, h)
        self.fire_range = fire_range
        print(f"Экземпляр класса с позывным '{self.call_sign}' создан.")

    @staticmethod
    def generate_coord() -> [int, int, int]:
        """Метод получения координат огневой позиции"""
        return CoordinateGenerator.generate_fire_coordinates()


class Signalman(FiringUnits):
    """Создание класса отвечающего за прием координат цели"""

    @staticmethod
    def take_coord(
        call_sign: str, target_number: int, target_coordinate: [int, int, int]
    ) -> str:
        """Метод подтверждения приема координат цели от подразделений разведки"""
        return (
            f"{call_sign} координаты цели № {target_number}:"
            f" x: {target_coordinate[0]}, y: {target_coordinate[1]}, "
            f"высота: {target_coordinate[2]} принял!"
        )


class Calculator:
    """Создание класса отвечающего за производство расчетов"""

    def __init__(self, call_sign: str, fire_range: int) -> None:
        """Инициализация объектов класса отвечающего за производство расчетов"""
        self.call_sign = call_sign
        self.fire_range = fire_range

    @classmethod
    def calculate_install(
        cls,
        target_coordinate: [int, int, int],
        fire_pos_coordinate: [int, int, int],
    ) -> float:
        """Метод вычисления дальности и дирекционного угла по цели
        для производства расчетов установок для стрельбы подразделением
        """
        zx = target_coordinate[0] - fire_pos_coordinate[0]
        zy = target_coordinate[1] - fire_pos_coordinate[1]
        target_distance = math.sqrt(zx**2 + zy**2)
        angle_rad = math.atan2(zy, zx)
        angle_deg = math.degrees(angle_rad)

        if angle_deg < 0:  # Корректировка дирекционного угла
            angle_deg += 360
            angle_mils = angle_deg / 6
            print(
                f"Дальность до цели - {target_distance:.2f} м,"
                f" дирекционный угол - {angle_mils:.2f} д.у."
            )
            return target_distance

    def is_within_range(self, target_distance: float) -> bool:
        """Метод проверки на принадлежность дальности до цели зоне поражения"""
        if self.fire_range > target_distance:
            return True
        return False


class GunCrew:
    """Инициализация класса отвечающего за готовность орудий"""

    def __init__(
        self, call_sign: str, target_number: int, amount_ammunition: int
    ) -> None:
        """Инициализация объектов класса отвечающего за готовность орудий"""
        self.call_sign = call_sign
        self.target_number = target_number
        self.amount_ammunition = amount_ammunition

    def guns_aim_to_target(self):
        """Метод отвечающий за готовность орудий к стрельбе"""
        return f"{self.call_sign} по цели {self.target_number} к стрельбе готов!"

    def change_pos(self, new_coord: [int, int, int]) -> str:
        """Метод отвечающий за готовность подразделения к перемещению (совершению марша)"""
        return (
            f"{self.call_sign} к перемещению в новый район ОП с координатами"
            f" {new_coord} готов!"
        )


class Firing(GunCrew):
    """Создание класса отвечающего ведение огня
    и текущий расход боеприпасов по цели
    """

    def __init__(
        self, call_sign: str, target_number: int, amount_ammunition: int
    ) -> None:
        """Инициализация объектов класса"""
        super().__init__(call_sign, target_number, amount_ammunition)
        self._total_ammunition_consumption = 0

    def keep_fire(self) -> None:
        """Метод отвечающий за ведение огня"""
        ammunition_consumption = 12
        print(
            f"{self.call_sign} по цели {self.target_number} огонь открыл!"
            f" Расход {ammunition_consumption}."
        )
        self._total_ammunition_consumption += ammunition_consumption

    @property
    def total_ammunition_consumption(self) -> int:
        """Метод отвечающий за общий расход боеприпасов по цели"""
        return self._total_ammunition_consumption

    @property
    def remaining_ammunition(self) -> int:
        """Метод отвечающий за остаток боеприпасов в подразделении"""
        remain = self.amount_ammunition - self._total_ammunition_consumption
        return remain


class SupportUnits(MovingUnits):
    """Создание объектов класса подразделений обеспечения"""

    def __init__(self, call_sign: str, x: int, y: int, h: int) -> None:
        """Инициализация объектов класса подразделений обеспечения"""
        super().__init__(call_sign, x, y, h)
        self.call_sign = call_sign
        print(f"Экземпляр класса с позывным '{self.call_sign}' создан.")

    @staticmethod
    def repair(ammunition: int, call_sign: str) -> int:
        """Метод проверки на необходимость пополнения боекомплекта"""
        if ammunition < 360:
            ammunition = 360
        print(
            f"Тех обслуживание и ремонт проведены. Боекомплект пополнен."
            f" {call_sign} к выполнению задач готов."
        )
        return ammunition


reconnaissance_unit = ArtilleryReconnaissance("Eyepiece", 15700, 57600, 170)
# reconnaissance_unit.move_to() # - проверка метода ручного ввода
# координат для подразделений разведки
recon_coord = reconnaissance_unit.generate_coord()
print(
    f"{reconnaissance_unit.call_sign} наблюдательный пункт с координатами"
    f" x: {recon_coord[0]}, y: {recon_coord[1]}, h: {recon_coord[2]}"
    f" на указанном рубеже занял."
)
target_coord = reconnaissance_unit.generate_target_coord()
target_num = reconnaissance_unit.generate_target_number()
print(
    f"{reconnaissance_unit.call_sign} координаты цели № {target_num}:"
    f" x: {target_coord[0]}, y: {target_coord[1]},"
    f" высота: {target_coord[2]} передал!"
)
print()
firing_unit = FiringUnits("Falcon", 80000, 25000, 160, 17500)
# firing_unit.move_to()  # проверка метода ручного ввода координат
# для огневых подразделений артиллерии
fire_pos_coord = firing_unit.generate_coord()
print(
    f"{firing_unit.call_sign} в район огневой позиции с координатами:"
    f" x: {fire_pos_coord[0]}, y: {fire_pos_coord[1]},"
    f" h: {fire_pos_coord[2]} прибыл."
)
coord_confirmation = Signalman.take_coord(
    firing_unit.call_sign, target_num, target_coord
)
print(coord_confirmation)
calculator = Calculator("Falcon", 17500)
target_dist = calculator.calculate_install(target_coord, fire_pos_coord)
if not calculator.is_within_range(target_dist):
    print(
        f"Цель № {target_num} вне зоны поражения {firing_unit.call_sign}"
        f" (превышение по дальности)."
    )
print()
firing_unit = FiringUnits("Dym", 80000, 25000, 160, 29500)
fire_pos_coord = firing_unit.generate_coord()
print(
    f"{firing_unit.call_sign} в район огневой позиции"
    f" с координатами: x: {fire_pos_coord[0]}, y: {fire_pos_coord[1]},"
    f" h: {fire_pos_coord[2]} прибыл."
)
coord_confirmation = Signalman.take_coord(
    firing_unit.call_sign, target_num, target_coord
)
print(coord_confirmation)
calculator = Calculator("Dym", 29500)
target_dist = calculator.calculate_install(target_coord, fire_pos_coord)
print()
fireman = Firing("Dym", target_num, 360)
readiness = fireman.guns_aim_to_target()
print(readiness)
fireman.keep_fire()
fireman.keep_fire()
fireman.keep_fire()
print(
    f"{firing_unit.call_sign} по цели {target_num} стрельбу закончил."
    f" Расход: {fireman.total_ammunition_consumption}."
)
print(f"Остаток боеприпасов на батарее: {fireman.remaining_ammunition}")
print()
support_unit = SupportUnits("Helper", 10000, 10000, 150)
support_unit_coord = fire_pos_coord
print(
    f"{support_unit.call_sign} в район координатами:"
    f" x: {support_unit_coord[0]}, y: {support_unit_coord[1]}"
    f" для проведения ТО и Р прибыл."
)
remain_ammunition = support_unit.repair(fireman.remaining_ammunition, fireman.call_sign)
print()
print(f"Остаток боеприпасов на батарее: {remain_ammunition}")
new_pos = fireman.change_pos(firing_unit.generate_coord())
print(new_pos)
