from abc import ABCMeta, abstractmethod


class ThirdPartyYoutubeLib(metaclass=ABCMeta):

    @abstractmethod 
    def list_videos(self) -> list[str]:
        pass 

    @abstractmethod
    def get_video_info(self, id: str) -> str:
        pass

    @abstractmethod 
    def download_video(self, id: str) -> str:
        pass


