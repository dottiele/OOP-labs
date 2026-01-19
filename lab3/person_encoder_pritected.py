
import json
import datetime as dt
from typing import Dict, List, Any, Set
from abc import ABC, abstractmethod
import uuid

class Serializable(ABC):
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass
    
    @classmethod
    @abstractmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Serializable':
        pass

class Person(Serializable):
    def __init__(self, name: str, born_in: dt.datetime) -> None:
        self._name = name
        self._friends: List[Person] = []
        self._born_in = born_in
        self._id = str(uuid.uuid4())
    
    def add_friend(self, friend: 'Person') -> None:
        if friend not in self._friends:
            self._friends.append(friend)
            friend.add_friend(self)
    
    # Публичные методы для доступа к приватным данным
    def get_name(self) -> str:
        return self._name
    
    def get_born_in(self) -> dt.datetime:
        return self._born_in
    
    def get_friends(self) -> List['Person']:
        return self._friends.copy()  # Возвращаем копию для защиты
    
    # Реализация интерфейса Serializable
    def to_dict(self) -> Dict[str, Any]:
        return {
            'name': self._name,
            'born_in': self._born_in.isoformat(),
            'friends': [friend._id for friend in self._friends],
            'id': self._id
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Person':
        person = cls(
            name=data['name'],
            born_in=dt.datetime.fromisoformat(data['born_in'])
        )
        person._id = data['id']
        return person