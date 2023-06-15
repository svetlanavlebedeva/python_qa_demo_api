import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


DOG_FILE_PATH = get_path(filename="tofu.jpg")
