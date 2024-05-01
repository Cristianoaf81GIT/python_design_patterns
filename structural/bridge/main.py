from clients import Remote  # pyright: ignore
from implementations import Tv, Radio  # pyright: ignore


def main() -> None:
    tv = Tv()
    radio = Radio()

    # remote control for tv
    remote_tv = Remote(device=tv)
    remote_radio = Remote(device=radio)

    remote_tv.toggle_power()
    remote_tv.channel_up()
    remote_tv.volume_up()

    remote_radio.toggle_power()
    remote_radio.channel_down()
    remote_radio.volume_up()
    remote_radio.volume_up()
    remote_radio.volume_down()


if __name__ == "__main__":
    main()
