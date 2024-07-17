from interfaces import ThirdPartyYoutubeLib # pyright:ignore


class ThirdPartyYoutubeClass(ThirdPartyYoutubeLib):

    _list_video: list[str] = []

    def list_videos(self) -> list[str]:
        self._list_video = ["video_1","video_2","video_3","video_4"]
        return self._list_video

    def get_video_info(self, id: str) -> str:
        if len(self._list_video) == 0:
            return "VIDEO_LIST_EMPTY"
        if id in self._list_video:
            return f"file type: ogg\nfile size: XXMB\nfile name: {id}\nlist_position: {self._list_video.index(id)}"
        return f"VIDEO_NOT_FOUND {id}"

    def download_video(self, id: str) -> str:
        self._list_video.append(id)
        return f"video successfully downloaded: {id}"
