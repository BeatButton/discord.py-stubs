import io
import threading
from typing import (
    Any,
    BinaryIO,
    Callable,
    ClassVar,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)
from typing_extensions import Literal

from .voice_client import VoiceClient

_FOA = TypeVar('_FOA', bound=FFmpegOpusAudio)
_MethodCallback = Callable[
    [Union[str, io.BufferedIOBase], str], Tuple[Optional[str], Optional[int]]
]
_OpusMethods = Literal['native', 'fallback']

class AudioSource:
    def read(self) -> bytes: ...
    def is_opus(self) -> bool: ...
    def cleanup(self) -> None: ...
    def __del__(self) -> None: ...

class PCMAudio(AudioSource):
    stream: BinaryIO
    def __init__(self, stream: BinaryIO) -> None: ...
    def read(self) -> bytes: ...

class FFmpegAudio(AudioSource):
    def __init__(
        self, source: Any, *, executable: str = ..., args: Any, **subprocess_kwargs: Any
    ) -> None: ...
    def cleanup(self) -> None: ...

class FFmpegPCMAudio(FFmpegAudio):
    @overload
    def __init__(
        self,
        source: io.BufferedIOBase,
        *,
        executable: str = ...,
        pipe: bool,
        stderr: Optional[BinaryIO] = ...,
        before_options: Optional[str] = ...,
        options: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        source: str,
        *,
        executable: str = ...,
        stderr: Optional[BinaryIO] = ...,
        before_options: Optional[str] = ...,
        options: Optional[str] = ...,
    ) -> None: ...
    def read(self) -> bytes: ...
    def is_opus(self) -> bool: ...

class FFmpegOpusAudio(FFmpegAudio):
    @overload
    def __init__(
        self,
        source: io.BufferedIOBase,
        *,
        bitrate: int = ...,
        codec: Optional[str] = ...,
        executable: str = ...,
        pipe: bool = ...,
        stderr: Optional[BinaryIO] = ...,
        before_options: Optional[str] = ...,
        options: Optional[str] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        source: str,
        *,
        bitrate: int = ...,
        codec: Optional[str] = ...,
        executable: str = ...,
        stderr: Optional[BinaryIO] = ...,
        before_options: Optional[str] = ...,
        options: Optional[str] = ...,
    ) -> None: ...
    @overload
    @classmethod
    async def from_probe(
        cls: Type[_FOA],
        source: io.BufferedIOBase,
        *,
        method: Optional[Union[_OpusMethods, _MethodCallback]] = ...,
        executable: str = ...,
        pipe: bool = ...,
        stderr: Optional[BinaryIO] = ...,
        before_options: Optional[str] = ...,
        options: Optional[str] = ...,
    ) -> _FOA: ...
    @overload
    @classmethod
    async def from_probe(
        cls: Type[_FOA],
        source: str,
        *,
        method: Optional[Union[_OpusMethods, _MethodCallback]] = ...,
        executable: str = ...,
        pipe: bool = ...,
        stderr: Optional[BinaryIO] = ...,
        before_options: Optional[str] = ...,
        options: Optional[str] = ...,
    ) -> _FOA: ...
    @overload
    @classmethod
    async def probe(
        cls,
        source: io.BufferedIOBase,
        *,
        method: Optional[Union[_OpusMethods, _MethodCallback]] = ...,
        executable: Optional[str] = ...,
    ) -> Tuple[Optional[str], Optional[int]]: ...
    @overload
    @classmethod
    async def probe(
        cls,
        source: str,
        *,
        method: Optional[Union[_OpusMethods, _MethodCallback]] = ...,
        executable: Optional[str] = ...,
    ) -> Tuple[Optional[str], Optional[int]]: ...
    def read(self) -> bytes: ...
    def is_opus(self) -> bool: ...

class PCMVolumeTransformer(AudioSource):
    original: AudioSource
    volume: float
    def __init__(self, original: AudioSource, volume: float = ...) -> None: ...
    def cleanup(self) -> None: ...
    def read(self) -> bytes: ...

class AudioPlayer(threading.Thread):
    DELAY: ClassVar[float] = ...

    daemon: bool
    source: AudioSource
    client: VoiceClient
    loops: int
    def run(self) -> None: ...
    def stop(self) -> None: ...
    def pause(self, *, update_speaking: bool = ...) -> None: ...
    def resume(self, *, update_speaking: bool = ...) -> None: ...
    def is_playing(self) -> bool: ...
    def is_paused(self) -> bool: ...
