from typing import Generic, TypeVar, List
T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        """Добавить элемент в стек"""
        self._items.append(item)
    
    def pop(self) -> T:
        """Удалить и вернуть верхний элемент"""
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._items.pop()
    
    def is_empty(self) -> bool:
        """Проверить, пуст ли стек"""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Вернуть размер стека"""
        return len(self._items)
    
    def peek(self) -> T:
        """Посмотреть верхний элемент без удаления"""
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._items[-1]