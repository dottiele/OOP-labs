
T = TypeVar('T')

class Queue(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def enqueue(self, item: T) -> None:
        """Добавить элемент в очередь"""
        self._items.append(item)
    
    def dequeue(self) -> T:
        """Удалить и вернуть первый элемент"""
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self._items.pop(0)
    
    def is_empty(self) -> bool:
        """Проверить, пуста ли очередь"""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Вернуть размер очереди"""
        return len(self._items)
    
    def peek(self) -> T:
        """Посмотреть первый элемент без удаления"""
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self._items[0]