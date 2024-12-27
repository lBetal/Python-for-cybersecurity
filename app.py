import hashlib
import os

def hash_file(file_path, algorithm='sha256'):
    if not os.path.isfile(file_path):
        return "Файл не найден. Убедитесь, что путь указан правильно."

    try:
        hasher = hashlib.new(algorithm)
    except ValueError:
        return f"Неподдерживаемый алгоритм: {algorithm}"

    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        return f"Ошибка при чтении файла: {e}"

# Пример использования
if __name__ == "__main__":
    file_path = input("Введите путь к файлу: ")
    algorithm = input("Введите алгоритм хеширования (например, md5, sha256, sha512): ").lower()

    result = hash_file(file_path, algorithm)
    print(f"Результат: {result}")