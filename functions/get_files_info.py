import os

def get_files_info(working_directory, directory="."):
  
  working_dir_abs = os.path.abspath(working_directory)
  target_dir = os.path.normpath(os.path.join(working_dir_abs, directory)) 
  
  # Will be True or False
  valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
  if not valid_target_dir:
    return f'Error: "{directory}" is not a directory'

  items = os.listdir(path=target_dir)
  
  output = ""
  try:
    for item in items:
      output += f"- {item}: file_size={os.path.getsize(os.path.join(target_dir, item))}bytes, is_dir={os.path.isdir(os.path.join(target_dir, item))}\n"
  except:
    return f"Error"
  
  return output