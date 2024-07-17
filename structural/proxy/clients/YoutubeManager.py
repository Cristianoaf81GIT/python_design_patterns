from interfaces import ThirdPartyYoutubeLib #pyright:ignore

class YoutubeManager:

    _service: ThirdPartyYoutubeLib
    _video_list: list[str] = []

    def __init__(self, service: ThirdPartyYoutubeLib) -> None:
        self._service = service

    def render_video_page(self, id: str) -> None:
        info = self._service.get_video_info(id)
        print(f"{info}")

    def render_list_panel(self) -> None:
        self._video_list = self._service.list_videos()
        print("video list:\n")
        for video in self._video_list:
            print(f"{video}\n")

    def on_user_input(self, id: str) -> None:        
        self.render_list_panel()
        self.render_video_page(id)


