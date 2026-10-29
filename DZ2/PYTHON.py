
from typing import Protocol, runtime_checkable
import random
from urllib.request import urlopen
from urllib.parse import urlencode
import json


@runtime_checkable
class TemperatureSensor(Protocol):
    def read_temperature(self) -> float:
        ...

    def get_sensor_id(self) -> str:
        ...


class WeatherAPISensor:
    def read_temperature(self) -> float:
        params = urlencode({
            "latitude": 46.4825,
            "longitude": 30.7233,
            "current": "temperature_2m"
        })

        url = f"https://api.open-meteo.com/v1/forecast?{params}"

        try:
            with urlopen(url, timeout=10) as response:
                data = json.loads(response.read().decode("utf-8"))

            temperature = data["current"]["temperature_2m"]
            return float(temperature)

        except Exception as error:
            raise RuntimeError(
                f"Не вдалося отримати температуру з API: {error}"
            ) from error

    def get_sensor_id(self) -> str:
        return "WAS26-Odesa"


class SimulatedSensor:
    def __init__(self, base: float, deviation: float):
        if deviation < 0:
            raise ValueError("Відхилення не може бути від'ємним")

        self.base = base
        self.deviation = deviation

    def read_temperature(self) -> float:
        return random.uniform(
            self.base - self.deviation,
            self.base + self.deviation
        )

    def get_sensor_id(self) -> str:
        return "SIM-001"


class FakeAlways25:
    def read_temperature(self) -> float:
        return 25.0

    def get_sensor_id(self) -> str:
        return "Fake-25"

class IndoorSensor:
    def __init__(self, room: str, temperature: float):
        self.room = room
        self.temperature = temperature

    def read_temperature(self) -> float:
        return float(self.temperature)

    def get_sensor_id(self) -> str:
        return f"INDOOR-{self.room}"


def display_sensor(sensor: TemperatureSensor) -> None:
    print(f"ID датчика: {sensor.get_sensor_id()}")
    print(f"Температура: {sensor.read_temperature():.1f} °C")
    print("-" * 30)


def main():
    sensors: list[TemperatureSensor] = [
        WeatherAPISensor(),
        SimulatedSensor(base=22.0, deviation=3.0),
        FakeAlways25(),
        IndoorSensor(room="101", temperature=23.5)
    ]

    for sensor in sensors:
        try:
            display_sensor(sensor)
        except (RuntimeError, ValueError) as error:
            print(f"Помилка датчика: {error}")


if __name__ == "__main__":
    main()

sensor = FakeAlways25()

print(isinstance(sensor, TemperatureSensor))
# True