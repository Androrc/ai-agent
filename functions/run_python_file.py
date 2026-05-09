import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):

    try:

            working_dir_abs = os.path.abspath(working_directory)

            target_dir = os.path.abspath(os.path.join(working_dir_abs, file_path))

            if not target_dir.startswith(working_dir_abs):
                 return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
                  
            if not os.path.isfile(target_dir):
                  return f'Error: "{file_path}" does not exist or is not a regular file'
            
            if not target_dir.endswith(".py"):
                  return f'Error: "{file_path}" is not a Python file'
            
            command = ["python", target_dir]

            if args:
                  command.extend(args)

            result = subprocess.run(
                    command,
                    cwd = working_dir_abs,
                    capture_output= True,
                    text = True,
                    timeout = 30
                    )
            
            output_parts = []

            if result.returncode != 0:
                  output_parts.append(f"Process exited with code {result.returncode}")

            if result.stderr == "" and result.stdout == "":
                  output_parts.append("No output produced")

            if result.stdout:
                  output_parts.append(f"STDOUT: {result.stdout}")

            if result.stderr:
                  output_parts.append(f"STDERR: {result.stderr}")

            return "\n".join(output_parts)
    
    except Exception as e:
      return f"Error: executing Python file: {e}"

# gemini chamando função
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file relative to the working directory, with optional command-line arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory",
            ),
            "args": types.Schema(
                  type=types.Type.ARRAY,
                  description="Optional command-line arguments to pass to the Python file",
                  items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["file_path"],
    ),
)

            
