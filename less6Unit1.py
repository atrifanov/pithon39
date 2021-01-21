from time import sleep
from datetime import datetime as dt

class TrafficLight:
    _states = {'красный': 7, 'желтый': 2, 'зеленый': 10}
    _color = ''

    def running(self):
        for color, sw_time in self._states.items():
            self._color = color
            start_state_time = dt.now()
            print(f"Светофор будет гореть '{self._color}' "
                  f"в течение {sw_time} секунд")
            sleep(sw_time)

if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()
