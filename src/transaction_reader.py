from typing import List, Dict  # Для Python < 3.9, иначе можно убрать
import pandas as pd
from pathlib import Path


def read_csv_transactions(path: str) -> list[dict[str, object]]:
    """
    Считывает транзакции из CSV-файла.

    Args:
        path (str): Путь к CSV-файлу.

    Returns:
        list[dict[str, object]]: Список словарей с транзакциями.
    """
    try:
        df = pd.read_csv(Path(path))  # Используем Path

        # Преобразуем DataFrame в список словарей.
        # to_dict(orient='records') уже делает то, что нужно:
        # каждую строку DataFrame преобразует в словарь.
        records = df.to_dict(orient="records")

        # Убедимся, что ключи словарей являются строками.
        # Это та самая строка, которая была изначально правильной
        # и которую нужно было вернуть, чтобы избежать ValueError.
        return [{str(k): v for k, v in row.items()} for row in records]
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути: {path}")
        return []
    except pd.errors.EmptyDataError:
        print(f"Ошибка: Файл CSV пуст: {path}")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении CSV-файла {path}: {e}")
        return []


def read_excel_transactions(path: str) -> list[dict[str, object]]:
    """
    Считывает транзакции из Excel-файла (.xlsx).

    Args:
        path (str): Путь к Excel-файлу.

    Returns:
        list[dict[str, object]]: Список словарей с транзакциями.
    """
    try:
        # Для чтения Excel требуется openpyxl. Убедитесь, что он установлен:
        # pip install openpyxl
        df = pd.read_excel(Path(path), engine="openpyxl")  # Используем Path

        # Преобразуем DataFrame в список словарей.
        records = df.to_dict(orient="records")

        # Убедимся, что ключи словарей являются строками.
        return [{str(k): v for k, v in row.items()} for row in records]
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути: {path}")
        return []
    except Exception as e:
        # Обратите внимание, что для Excel нет pd.errors.EmptyDataError
        # (или она обрабатывается по-другому), поэтому здесь остается общий Exception.
        print(f"Произошла ошибка при чтении Excel-файла {path}: {e}")
        return []


# --- Пример использования кода ---
if __name__ == "__main__":
    # Создадим фиктивные файлы для тестирования.
    # Убедитесь, что pip install pandas openpyxl выполнены.

    csv_test_file = "sample_transactions.csv"
    excel_test_file = "sample_transactions.xlsx"
    empty_csv_file = "empty.csv"

    # Создаем фиктивный CSV-файл
    csv_content = """id,amount,currency,date
1,100.50,USD,2023-01-15
2,25.00,EUR,2023-01-16
3,75.20,GBP,2023-01-17
"""
    try:
        with open(csv_test_file, "w", encoding="utf-8") as f:
            f.write(csv_content)
        print(f"Создан тестовый CSV-файл: {csv_test_file}")
    except Exception as e:
        print(f"Не удалось создать CSV-файл: {e}")

    # Создаем фиктивный Excel-файл (требуется openpyxl)
    try:
        df_excel_test = pd.DataFrame(
            {
                "id": [4, 5],
                "amount": [50.0, 120.75],
                "currency": ["JPY", "CHF"],
                "date": ["2023-01-18", "2023-01-19"],
            }
        )
        df_excel_test.to_excel(excel_test_file, index=False, engine="openpyxl")
        print(f"Создан тестовый Excel-файл: {excel_test_file}")
    except ImportError:
        print(
            "\nВнимание: Для создания и чтения Excel-файлов требуется 'openpyxl'. "
            "Пожалуйста, установите: pip install openpyxl"
        )
        print(f"Excel-файл '{excel_test_file}' не был создан.")
        # Удаляем пустой файл, если он был создан до ошибки openpyxl
        Path(excel_test_file).unlink(missing_ok=True)
    except Exception as e:
        print(f"Не удалось создать Excel-файл: {e}")

    # Создаем пустой CSV-файл для теста на EmptyDataError
    try:
        Path(empty_csv_file).touch()
        print(f"Создан пустой CSV-файл: {empty_csv_file}")
    except Exception as e:
        print(f"Не удалось создать пустой CSV-файл: {e}")

    print("\n--- Тестирование функций чтения ---")

    print("\n--- Чтение CSV ---")
    csv_transactions = read_csv_transactions(csv_test_file)
    if csv_transactions:
        print("Данные из CSV:")
        for t in csv_transactions:
            print(t)
    else:
        print("CSV-файл не удалось прочитать или он пуст.")

    print("\n--- Чтение Excel ---")
    excel_transactions = read_excel_transactions(excel_test_file)
    if excel_transactions:
        print("Данные из Excel:")
        for t in excel_transactions:
            print(t)
    else:
        print("Excel-файл не удалось прочитать или произошла ошибка.")

    print("\n--- Тестирование несуществующего файла CSV ---")
    read_csv_transactions("non_existent_file.csv")

    print("\n--- Тестирование пустого файла CSV ---")
    read_csv_transactions(empty_csv_file)

    # --- Очистка тестовых файлов ---
    print("\n--- Очистка тестовых файлов ---")
    Path(csv_test_file).unlink(missing_ok=True)
    Path(excel_test_file).unlink(missing_ok=True)
    Path(empty_csv_file).unlink(missing_ok=True)
    print("Тестовые файлы удалены.")
