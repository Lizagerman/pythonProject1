import functools
import logging
import sys
from typing import Optional, Any


import functools
import logging
import sys
from typing import Any, Callable, Optional





def log(filename: Optional[str] = None):
    # Настройка логирования
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    if filename:
        handler = logging.FileHandler(filename)
    else:
        handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logger.info(f'Calling function: {func.__name__} with args: {args} and kwargs: {kwargs}')
                result = func(*args, **kwargs)
                logger.info(f'Function: {func.__name__} returned: {result}')
                return result
            except Exception as e:
                logger.error(f'Function: {func.__name__} raised an error: {type(e).__name__} with args: {args}')
                raise e

        return wrapper

    return decorator






def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования выполнения функции.

    :param filename: Имя файла для записи логов. Если None, выводит в консоль.
    """
    # Настройка логирования
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    if filename:
        handler = logging.FileHandler(filename)
    else:
        handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                logger.info(f'Вызов функции {func.__name__} с аргументами {args} и {kwargs}')
                result = func(*args, **kwargs)
                logger.info(f'Функция {func.__name__} вернула результат: {result}')
                return result
            except Exception as e:
                logger.error(f'Ошибка в функции {func.__name__}: {type(e).__name__} - {e}. Аргументы: {args}, {kwargs}')
                raise  # Повторно выбрасываем исключение после логирования

        return wrapper

    return decorator

