from lib import ThirdPartyYoutubeClass #pyright: ignore
from proxies import CachedYoutubeClass #pyright: ignore
from clients import YoutubeManager #pyright: ignore


def main() -> None:
    youtube_service = ThirdPartyYoutubeClass()
    youtube_class = CachedYoutubeClass(service=youtube_service)
    manager = YoutubeManager(service=youtube_class)
    manager.on_user_input(id="video_1")


if __name__ == "__main__":
    main()