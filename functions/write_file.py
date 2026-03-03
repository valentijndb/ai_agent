import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite files",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="relative file_path of file",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="content to be written",
            )
        },
        required=["file_path","content"]
    ),
)

def write_file(working_directory, file_path, content):
  try:
      abs_working_dir = os.path.abspath(working_directory)
      target_dir = os.path.normpath(os.path.join(abs_working_dir, file_path))
      if os.path.commonpath([abs_working_dir, target_dir]) != abs_working_dir:
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
      if os.path.isdir(target_dir):
        return f'Error: "Cannot write to "{file_path}" as it is a directory'
      
      os.makedirs(file_path, exist_ok=True)
      with open(target_dir,"w") as file:
         file.write(content)
      
      return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
     
  except Exception as e:
      return f"Error: {e}"