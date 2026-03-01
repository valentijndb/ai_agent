import os
import subprocess

def run_python_file(working_directory, file_path, args=None):

  try:

    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abs_working_dir, file_path))
    if os.path.commonpath([abs_working_dir, target_dir]) != abs_working_dir:
      return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_dir):
      return f'Error: "{file_path}" does not exist or is not a regular file'
    if not file_path.endswith(".py"):
      return f'Error: "{file_path}" is not a Python file'
    
    command = ["python", os.path.normpath(os.path.join(abs_working_dir, file_path))]
    
    if args != None:
      command.extend(args)
    subproc =subprocess.run(command, text=True, timeout=30, capture_output=True)
    
    if subproc.returncode != 0:
      return f"Process exited with code {subproc.returncode}"
    
    if subproc.stdout == "" and subproc.stderr == "":
      return "No output produced"
    else:
      return f"STDOUT: {subproc.stdout} \n STDERR: {subproc.stderr}"
     
  
  except Exception as e:
    return f"Error: {e}"