import sys
from typing import Any, BinaryIO, ClassVar, FrozenSet, Union
from typing_extensions import Final

if sys.version_info >= (3, 6):
    from os import PathLike

VALID_STATIC_FORMATS: Final[FrozenSet[str]] = ...
VALID_AVATAR_FORMATS: Final[FrozenSet[str]] = ...

class Asset:
    BASE: ClassVar[str]
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    async def read(self) -> bytes: ...
    if sys.version_info >= (3, 6):
        async def save(
            self, fp: Union[BinaryIO, PathLike[str], str], *, seek_begin: bool = ...
        ) -> int: ...
    else:
        async def save(
            self, fp: Union[BinaryIO, str], *, seek_begin: bool = ...
        ) -> int: ...