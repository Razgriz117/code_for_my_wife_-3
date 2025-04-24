class CompileCommand:
    def __init__(self, file_name, file_path, output_file_name, output_file_path, compiler, arguments=None, includes=None):
        self.FileName = file_name
        self.FilePath = file_path
        self.OutputFileName = output_file_name
        self.OutputFilePath = output_file_path
        self.Compiler = compiler
        self.Arguments = arguments if arguments is not None else {}
        self.Includes = includes if includes is not None else {}

    def __repr__(self):
        return (f"CompileCommand(FileName='{self.FileName}', "
                f"FilePath='{self.FilePath}', "
                f"OutputFileName='{self.OutputFileName}', "
                f"OutputFilePath='{self.OutputFilePath}', "
                f"Compiler='{self.Compiler}', "
                f"Arguments={self.Arguments}, "
                f"Includes={self.Includes})")