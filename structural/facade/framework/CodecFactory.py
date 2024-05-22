from dataclasses import dataclass
from .VideoFile import VideoFile
from .Mpeg4CompressionCodec import Mpeg4CompressionCodec
from .OggCompressionCodec import OggCompressionCodec
from .CompressionCodec import CompressionCodec


@dataclass(kw_only=True)
class CodecFactory:

    def extract(self, video: VideoFile) -> CompressionCodec:
        print(
            f"extracting audio and video codecs from video file: {video.get_file_name()}"  # noqa
        )  # noqa

        extension = video.get_file_name().split(".")[1]

        if "mp4" in extension:
            return Mpeg4CompressionCodec()
        else:
            return OggCompressionCodec()
