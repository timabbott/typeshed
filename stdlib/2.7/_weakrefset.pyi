from typing import Iterator, Any

class WeakSet:
    def __iter__(self) -> Iterator[Any]: ...
    def add(self, *args, **kwargs) -> Any: ...
