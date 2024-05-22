from dataclasses import dataclass
from typing import Literal
from framework import (  # pyright: ignore
    BitRateReader,
    OggCompressionCodec,
    Mpeg4CompressionCodec,
    VideoFile,
    AudioMixer,
    CompressionCodec,
    CodecFactory,
    File,
)


@dataclass(kw_only=True)
class VideoConverterFacade:

    def convert_video(
        self, filename: str, format: Literal["mp4", "ogg"]
    ) -> File:  # noqa
        file = VideoFile(filename=filename)
        codec_factory = CodecFactory()
        source_codec = codec_factory.extract(video=file)
        destination_codec: CompressionCodec

        if format == "mp4":
            destination_codec = Mpeg4CompressionCodec()
        else:
            destination_codec = OggCompressionCodec()

        bit_rate_src = BitRateReader(filename=filename)
        bit_rate_src.read(source_codec=source_codec)

        bit_rate_result = BitRateReader(filename=filename)
        bit_rate_result.convert(
            buffer=bit_rate_src, destination_codec=destination_codec
        )  # noqa

        AudioMixer().fix(data=bit_rate_result)

        return File(filename=bit_rate_result.get_file())
