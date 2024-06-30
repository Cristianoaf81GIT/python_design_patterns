from faker import Faker
from faker.providers import python
from models import Channel  # pyright: ignore
from interfaces import DeviceInterface  # pyright: ignore


class Remote:

    _device: DeviceInterface
    _fake: Faker = Faker()

    def __init__(self, device: DeviceInterface) -> None:
        self._device = device

    def toggle_power(self) -> None:
        if self._device.is_enabled() is False:
            self._device.enable()
        else:
            self._device.disable()
        print(f"{self._device.__repr__()} is on ? {self._device.is_enabled()}")

    def volume_up(self) -> None:
        current_volume = self._device.get_volume()
        current_volume += 0.5
        self._device.set_volume(current_volume)
        print(f"volume up to: {current_volume}")

    def volume_down(self) -> None:
        current_volume = self._device.get_volume()
        current_volume -= 0.5
        self._device.set_volume(current_volume)
        print(f"volume down to: {current_volume}")

    def channel_down(self) -> None:
        channel_name = self._fake.name()
        self._fake.add_provider(python)
        channel_frequeny = self._fake.pyfloat()
        new_channel = Channel(frequency=channel_frequeny, name=channel_name)
        self._device.set_channel(channel=new_channel)
        print(f"current channel: {new_channel.__repr__()}")

    def channel_up(self) -> None:
        channel_name = self._fake.name()
        self._fake.add_provider(python)
        channel_frequeny = self._fake.pyfloat()
        new_channel = Channel(frequency=channel_frequeny, name=channel_name)
        self._device.set_channel(channel=new_channel)
        print(f"current channel: {new_channel.__repr__()}")
