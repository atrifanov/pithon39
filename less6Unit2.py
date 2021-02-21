class Road:
    _gravity: float = 0.02

    def __init__(self, length: [int, float], width: [int, float]):
        self._length = float(length)
        self._width = float(width)

    def get_gravity(self, thickness):
        try:
            return (self._length * self._width
                    * thickness * self._gravity)
        except TypeError:
            return None

if __name__ == '__main__':
    try:
        road = Road(input('Введите длину дороги, м '), input('Введите ширину дороги, м '))
        print(
            'Масса дорожного покрытия составит:',
            road.get_gravity(int(input('Введите толщину дороги, см '))),
            'тонн'
        )
    except TypeError:
        print('класс Road требует 2 аргумента')
