

T = TypeVar('T')

# Тип: очередь представляется как список
Queue = List[T]

def create_queue() -> Queue:
    """Создать пустую очередь"""
    return []

def enqueue(queue: Queue[T], item: T) -> Queue[T]:
    """Добавить элемент в очередь"""
    return queue + [item]

def dequeue(queue: Queue[T]) -> Tuple[Optional[T], Queue[T]]:
    """Удалить и вернуть первый элемент"""
    if is_empty(queue):
        return None, queue
    return queue[0], queue[1:]

def is_empty(queue: Queue[T]) -> bool:
    """Проверить, пуста ли очередь"""
    return len(queue) == 0

def size(queue: Queue[T]) -> int:
    """Вернуть размер очереди"""
    return len(queue)

def peek(queue: Queue[T]) -> Optional[T]:
    """Посмотреть первый элемент без удаления"""
    if is_empty(queue):
        return None
    return queue[0]