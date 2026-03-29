class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self.capacity = capacity
        self._data: dict[str, str] = {}

    def get(self, key: str) -> str:
        if key not in self._data:
            return ""

        value = self._data.pop(key)
        self._data[key] = value
        return value

    def set(self, key: str, value: str) -> None:
        if key in self._data:
            self._data.pop(key)
        elif len(self._data) >= self.capacity:
            oldest_key = next(iter(self._data))
            self._data.pop(oldest_key)

        self._data[key] = value

    def rem(self, key: str) -> None:
        self._data.pop(key, None)