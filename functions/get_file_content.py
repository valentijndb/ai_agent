import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
  
  try:
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abs_working_dir, file_path))
    if os.path.commonpath([abs_working_dir, target_dir]) != abs_working_dir:
      return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" is not a file'
    
    with open(target_dir, "r") as file:
      content = file.read(MAX_CHARS)

      if file.read(1):
        content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    
    return content
  
  except Exception as e:
    return f"Error: {e}"