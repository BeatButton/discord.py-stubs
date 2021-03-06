import asyncio
from typing import Any, ClassVar, List, Mapping, Optional, Tuple, Union, overload

import aiohttp

from .activity import BaseActivity
from .client import Client
from .enums import Status
from .flags import Intents, MemberCacheFlags
from .guild import Guild
from .mentions import AllowedMentions

class EventType:
    close: ClassVar[int] = ...
    reconnect: ClassVar[int] = ...
    resume: ClassVar[int] = ...
    identify: ClassVar[int] = ...
    terminate: ClassVar[int] = ...
    clean_close: ClassVar[int] = ...

class Shard:
    @property
    def id(self) -> int: ...
    def launch(self) -> None: ...
    async def close(self) -> None: ...
    async def disconnect(self) -> None: ...
    async def worker(self) -> None: ...
    async def reidentify(self, exc: BaseException) -> None: ...
    async def reconnect(self) -> None: ...

class ShardInfo:
    id: int
    shard_count: Optional[int]
    def is_closed(self) -> bool: ...
    async def disconnect(self) -> None: ...
    async def reconnect(self) -> None: ...
    async def connect(self) -> None: ...
    @property
    def latency(self) -> float: ...
    def is_ws_ratelimited(self) -> bool: ...

class AutoShardedClient(Client):
    shard_ids: Optional[Union[List[int], Tuple[int]]]
    @overload
    def __init__(
        self,
        *args: Any,
        shard_ids: Union[List[int], Tuple[int]],
        shard_count: int,
        max_messages: Optional[int] = ...,
        loop: Optional[asyncio.AbstractEventLoop] = ...,
        connector: aiohttp.BaseConnector = ...,
        proxy: Optional[str] = ...,
        proxy_auth: Optional[aiohttp.BasicAuth] = ...,
        intents: Optional[Intents] = ...,
        member_cache_flags: Optional[MemberCacheFlags] = ...,
        fetch_offline_members: bool = ...,
        chunk_guilds_at_startup: bool = ...,
        status: Optional[Status] = ...,
        activity: Optional[BaseActivity] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
        heartbeat_timeout: float = ...,
        guild_ready_timeout: float = ...,
        guild_subscriptions: bool = ...,
        assume_unsync_clock: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *args: Any,
        shard_ids: None = ...,
        shard_count: Optional[int] = ...,
        max_messages: Optional[int] = ...,
        loop: Optional[asyncio.AbstractEventLoop] = ...,
        connector: aiohttp.BaseConnector = ...,
        proxy: Optional[str] = ...,
        proxy_auth: Optional[aiohttp.BasicAuth] = ...,
        intents: Optional[Intents] = ...,
        member_cache_flags: Optional[MemberCacheFlags] = ...,
        fetch_offline_members: bool = ...,
        chunk_guilds_at_startup: bool = ...,
        status: Optional[Status] = ...,
        activity: Optional[BaseActivity] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
        heartbeat_timeout: float = ...,
        guild_ready_timeout: float = ...,
        guild_subscriptions: bool = ...,
        assume_unsync_clock: bool = ...,
    ) -> None: ...
    @property
    def latency(self) -> float: ...
    @property
    def latencies(self) -> List[Tuple[int, float]]: ...
    def get_shard(self, shard_id: int) -> Optional[ShardInfo]: ...
    @property
    def shards(self) -> Mapping[int, ShardInfo]: ...
    async def request_offline_members(self, *guilds: Guild) -> None: ...
    async def launch_shard(
        self, gateway: str, shard_id: int, *, initial: bool = ...
    ) -> None: ...
    async def launch_shards(self) -> None: ...
    async def connect(self, *, reconnect: bool = ...) -> None: ...
    async def close(self) -> None: ...
    async def change_presence(
        self,
        *,
        activity: Optional[BaseActivity] = ...,
        status: Optional[Status] = ...,
        afk: bool = ...,
        shard_id: Optional[int] = ...,
    ) -> None: ...
    def is_ws_ratelimited(self) -> bool: ...
