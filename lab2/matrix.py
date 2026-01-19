
from typing import List, Union, overload
from __future__ import annotations

class Matrix:
    def __init__(self, data: List[List[float]]) -> None:
        self._validate_matrix(data)
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0
    
    def _validate_matrix(self, data: List[List[float]]) -> None:
        """Проверка корректности матрицы"""
        if not data:
            raise ValueError("Матрица не может быть пустой")
        row_len = len(data[0])
        for row in data:
            if len(row) != row_len:
                raise ValueError("Все строки матрицы должны быть одинаковой длины")
    
    def __add__(self, other: Matrix) -> Matrix:
        """Сложение матриц"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матриц должны совпадать для сложения")
        
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)
    
    def __mul__(self, other: Union[Matrix, float]) -> Matrix:
        """Умножение матрицы на матрицу или на скаляр"""
        if isinstance(other, (int, float)):
            # Умножение на скаляр
            result = [
                [self.data[i][j] * other for j in range(self.cols)]
                for i in range(self.rows)
            ]
            return Matrix(result)
        elif isinstance(other, Matrix):
            # Умножение матриц
            if self.cols != other.rows:
                raise ValueError(
                    f"Количество столбцов первой матрицы ({self.cols}) "
                    f"должно совпадать с количеством строк второй ({other.rows})"
                )
            
            result = [
                [
                    sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                    for j in range(other.cols)
                ]
                for i in range(self.rows)
            ]
            return Matrix(result)
        else:
            raise TypeError("Неподдерживаемый тип для умножения")
    
    def transpose(self) -> Matrix:
        """Транспонирование матрицы"""
        result = [
            [self.data[j][i] for j in range(self.rows)]
            for i in range(self.cols)
        ]
        return Matrix(result)
    
    def __str__(self) -> str:
        return "\n".join([" ".join(map(str, row)) for row in self.data])
    
    def __repr__(self) -> str:
        return f"Matrix({self.data})"