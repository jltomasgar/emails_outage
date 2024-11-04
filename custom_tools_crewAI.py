from crewai_tools import BaseTool
import time
import os


class file_writer(BaseTool):
    name: str = "File writer"
    description: str = "Writes contents to a local file. "
    def _run(self, file_name: str, contents: str) -> str:
        try:
            with open(file_name, "w") as f:
                f.write(contents)
            print(f"File written to {file_name}.")
            return contents
        except Exception:
            return "Failed to save contents."



class file_writer2(BaseTool):
    name: str = "File writer"
    description: str = "Saves text contents to a file, both given as inputs. "
    def _run(self, contents: str, file_path: str) -> dict:
        try:
            if not os.path.exists('extracted_fields'):
                os.makedirs('extracted_fields')
            with open("./extracted_fields/"+file_path, "w") as f:
                f.write(contents)
            print(f"File written to {file_path}.")
            return contents
        except Exception:
            return "Failed to save configuration files."

