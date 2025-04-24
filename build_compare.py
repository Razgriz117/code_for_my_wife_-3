import json
import os

def load_compile_commands(json_path):
    with open(json_path, 'r') as f:
        compile_db = json.load(f)

    command_dict = {}

    for entry in compile_db:
        file_path = os.path.abspath(entry['file'])
        file_name = os.path.basename(file_path)

        output_path = entry.get('output', None)
        output_file_name = os.path.basename(output_path) if output_path else None
        output_file_path = os.path.dirname(os.path.abspath(output_path)) if output_path else None

        command_parts = entry['command'].split()
        compiler = command_parts[0]
        raw_args = command_parts[1:]

        args = {}
        includes = {}

        for arg in raw_args:
            if arg.startswith("-I"):
                include_path = arg[2:]
                include_file = os.path.basename(include_path)
                includes[include_file] = include_path
            elif '=' in arg:
                key, value = arg.split('=', 1)
                args[key] = value
            else:
                args[arg] = True

        cmd = CompileCommand(
            file_name=file_name,
            file_path=file_path,
            output_file_name=output_file_name,
            output_file_path=output_file_path,
            compiler=compiler,
            arguments=args,
            includes=includes
        )

        command_dict[file_path] = cmd

    return command_dict