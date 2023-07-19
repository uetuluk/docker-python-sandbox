# from RestrictedPython import compile_restricted as compile

# from RestrictedPython import safe_builtins
# from RestrictedPython import limited_builtins
# from RestrictedPython import utility_builtins
import sys
from io import StringIO
import traceback
import ast


class CodeExecutor:
    def __init__(self):
        self.locals = {}

    def execute_code(self, code_string: str) -> str:
        output = StringIO()
        code = ast.parse(code_string, mode='exec')

        try:
            sys.stdout = output
            for node in code.body:
                if isinstance(node, ast.Expr):  # an expression, to be evaluated
                    result = eval(compile(ast.Expression(
                        node.value), '<string>', 'eval'), self.locals)
                    if result is not None:
                        print(result)
                else:  # a statement, to be executed
                    exec(compile(ast.fix_missing_locations(ast.Module(
                        [node], [])), '<string>', 'exec'), self.locals)

        except:
            return traceback.format_exc()
        finally:
            sys.stdout = sys.__stdout__

        return output.getvalue()


code_executor = CodeExecutor()


def run(code_string: str) -> str:
    # byte_code = compile(code_string, '<inline code>', 'exec')
    # exec(byte_code, {'__builtins__': safe_builtins}, None)
    print(code_string)

    code_executor_result = code_executor.execute_code(code_string)

    if code_executor_result:
        return code_executor_result

    return "Code executed successfully."
