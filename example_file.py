"""Файл, в котором намерено допускаем ошибки, чтобы проверить pre-commit."""

# STDLIB
from datetime import datetime


a = 2
aboba_text = "aboba"


def aboba(x1: int, x2: int) -> bool:
    """Функция что-то делает.

    Args:
        x1(int): первый аргумент.
        x2(int): второй аргумент.

    Returns:
        bool: Истина всегда.

    """
    return True


a = a + 1
print("Строка с одинарными кавычками")
print("Строка с двойными кавычками")
print(a)
print(f"Сейчас время - {datetime.now()}")
