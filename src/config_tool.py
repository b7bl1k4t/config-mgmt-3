import sys
import yaml
from parser import convert_to_custom_format, validate_syntax

def main():
    if len(sys.argv) != 2:
        print("Usage: python config_tool.py <path_to_yaml>")
        sys.exit(1)

    input_path = sys.argv[1]

    try:
        with open(input_path, 'r', encoding='utf-8-sig') as file:
            yaml_content = yaml.safe_load(file)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)

    try:
        validate_syntax(yaml_content)
    except SyntaxError as e:
        print(f"Синтаксическая ошибка: {e}")
        sys.exit(1)

    output = convert_to_custom_format(yaml_content)
    print(output)

if __name__ == "__main__":
    main()
