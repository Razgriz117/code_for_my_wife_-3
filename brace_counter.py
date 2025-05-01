import json

def load_compile_commands_with_lineno(path):
    entries = []
    with open(path, 'r', encoding='utf-8') as f:
        brace_depth = 0
        buffer = []
        start_line = None

        for lineno, line in enumerate(f, 1):
            # look for the start of an object
            if brace_depth == 0 and '{' in line:
                start_line = lineno
            # track braces
            brace_depth += line.count('{')
            brace_depth -= line.count('}')
            if brace_depth > 0:
                buffer.append(line)
            # when we close the object
            if start_line is not None and brace_depth == 0:
                json_text = ''.join(buffer)
                entry = json.loads(json_text)
                entries.append((start_line, entry))
                buffer = []
                start_line = None

    return entries

# Example:
for line, cmd in load_compile_commands_with_lineno('compile_commands.json'):
    print(f"{cmd['file']} defined starting at line {line}")