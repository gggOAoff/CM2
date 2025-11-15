# Визуализация графа зависимостей для менеджера пакетов

## Общее описание
Инструмент визуализации графа зависимостей для менеджера пакетов, реализованный на языке python.

## Функции
- **Функция Parse:** парсинг данных из файла Config.xml
- **Функция Print:** вывод всех параметров, настраиваемых пользователем
- **Функция Get:** поиск и получение тега в xml файле

## Сборка и запуск
```bash
python CM2.py
```

## Тестирование и примеры использования

### Тест с test_path и mode в Config.xml
```bash
package:
    name = Test
    version = 1.0.1

repository:
    mode = Mode1
    test_path = TestRepo.xml

output:
    filename = graph

filters:
    substring = Test
```

### Тест с url в Config.xml
```bash
package:
    name = Test
    version = 1.0.1

repository:
    url = Link

output:
    filename = graph

filters:
    substring = Test
```

### Тест обработки ошибок: test_path в Config.xml без mode
```bash
    Отсутствует режим для тестового репозитория
```