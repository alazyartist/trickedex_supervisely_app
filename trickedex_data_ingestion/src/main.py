import time
from dotenv import load_dotenv
import os
import supervisely as sly



def main():
    if sly.is_development():
        load_dotenv("local.env")
        load_dotenv(os.path.expanduser("./../supervisely.env"))
    api = sly.Api.from_env(env_file='./../supervisely.env')
    
    
    print(f"loaded {api}")

    workspace_id = sly.env.workspace_id()
    project = api.project.create(workspace_id,"Tricks",type=sly.ProjectType.VIDEOS, change_name_if_conflict=True)
    print(project)


if __name__ == "__main__":
    print("started")
    main()