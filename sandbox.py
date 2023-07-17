# from RestrictedPython import compile_restricted as compile

# from RestrictedPython import safe_builtins
# from RestrictedPython import limited_builtins
# from RestrictedPython import utility_builtins
import sys
from io import StringIO


def run(code_string: str) -> str:
    try:
        # byte_code = compile(code_string, '<inline code>', 'exec')
        # exec(byte_code, {'__builtins__': safe_builtins}, None)
        stdout_backup = sys.stdout
        sys.stdout = StringIO()

        exec(code_string, None)

        console_output = sys.stdout.getvalue()
        sys.stdout = stdout_backup

        if console_output:
            return console_output

        return "Code executed successfully."

    except Exception as error:
        print(error)
