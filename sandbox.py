# from RestrictedPython import compile_restricted as compile

# from RestrictedPython import safe_builtins
# from RestrictedPython import limited_builtins
# from RestrictedPython import utility_builtins
import sys
from io import StringIO, BytesIO
import traceback
import ast
import matplotlib.pyplot as plt
import base64
import builtins
import importlib


class CodeExecutor:
    def __init__(self):
        self.locals = {}
        self.original_import = builtins.__import__

        # Handle matplotlib plots

        def custom_show(original_show):
            def show(*args, **kwargs):
                buf = BytesIO()
                plt.savefig(buf, format='png')
                buf.seek(0)
                print(base64.b64encode(buf.read()).decode('utf-8'))
                return original_show(*args, **kwargs)
            return show

        def custom_import(name, *args, **kwargs):
            module = self.original_import(name, *args, **kwargs)
            if "matplotlib.pyplot" in name:
                module.pyplot.show = custom_show(module.pyplot.show)
            return module

        builtins.__import__ = custom_import

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
            plt.close('all')

        except:
            return traceback.format_exc()
        finally:
            sys.stdout = sys.__stdout__
        # print(self.locals)
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
