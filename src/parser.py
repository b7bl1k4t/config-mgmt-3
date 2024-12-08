import re

class SyntaxError(Exception):
    """Класс исключения для синтаксических ошибок."""
    pass

def validate_name(name):
    """Проверяет, соответствует ли имя правилам."""
    pattern = r'^[_A-Z][_a-zA-Z0-9]*$'
    if not re.match(pattern, name):
        raise SyntaxError(f"Некорректное имя: '{name}'. Имена должны соответствовать паттерну '{pattern}'.")

def validate_value(value):
    """Рекурсивно проверяет значение на соответствие допустимым типам."""
    if isinstance(value, (int, float)):
        return
    elif isinstance(value, str):
        return
    elif isinstance(value, list):
        for item in value:
            validate_value(item)
    else:
        raise SyntaxError(f"Недопустимый тип значения: {type(value)}. Допустимые типы: числа, строки, массивы.")

def validate_syntax(yaml_content):
    """Проверяет синтаксис YAML-контента на соответствие правилам."""
    if not isinstance(yaml_content, dict):
        raise SyntaxError("Верхний уровень YAML-файла должен быть объектом (ключ-значение).")
    for key, value in yaml_content.items():
        validate_name(key)
        validate_value(value)
    return True

def convert_to_custom_format(yaml_content):
    result = []
    for key, value in yaml_content.items():
        line = f"{key} := {parse_value(value)}"
        result.append(line)
    return "\n".join(result)

def parse_value(value):
    if isinstance(value, str):
        # Экранируем кавычки внутри строки
        escaped_value = value.replace('"', r'\"')
        return f'@"{escaped_value}"'
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, list):
        if not value:
            return '[]'  # Пустой массив
        else:
            items = " ".join(parse_value(v) for v in value)
            return f"[ {items} ]"
    else:
        raise SyntaxError(f"Недопустимый тип значения: {type(value)}")
