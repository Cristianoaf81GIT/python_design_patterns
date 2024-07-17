from interfaces import ThirdPartyYoutubeLib #pyright: ignore


class CachedYoutubeClass(ThirdPartyYoutubeLib):


    _service: ThirdPartyYoutubeLib
    _list_cached: list[str] = []
    _video_cached_info: str = ""
    _downloaded_video_path: str = ""
    need_reset: bool = False


    def __init__(self, service: ThirdPartyYoutubeLib) -> None:
        self._service = service


    def list_videos(self) -> list[str]:
        if len(self._list_cached) == 0 or self.need_reset:
            self._list_cached = self._service.list_videos()
        return self._list_cached


    def get_video_info(self, id: str) -> str:
        if self._video_cached_info.strip() == "" or self.need_reset:
            self._video_cached_info = self._service.get_video_info(id=id)
        return self._video_cached_info

    def download_video(self, id: str) -> str:
        if self._downloaded_video_path.strip() == "" or self.need_reset:
            self._downloaded_video_path = self._service.download_video(id)
        return self._downloaded_video_path
        
