from clients import VideoConverterFacade  # pyright: ignore


def main() -> None:
    converter = VideoConverterFacade()
    mp4 = converter.convert_video(filename="bunny.ogg", format="mp4")
    mp4.write()

    ogg = converter.convert_video(filename="robot.mp4", format="ogg")
    ogg.write()


if __name__ == "__main__":
    main()
