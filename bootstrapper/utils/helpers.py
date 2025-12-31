import shutil
import os

def copy_template(template_type: str, project_name: str):
    src = os.path.join(os.path.dirname(__file__), "..", "..", "templates", template_type)
    dst = os.path.join(os.getcwd(), project_name)
    if os.path.exists(dst):
        raise FileExistsError(f"Directory {project_name} already exists")
    shutil.copytree(src, dst)
    print(f"Copied {template_type} template into {project_name}/")
