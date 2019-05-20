import platform
import os

from pathlib import Path


def get_log_file_dir(subdir: str=None) -> str:
    current_system = platform.system()

    if current_system == 'Windows':
        log_dir = str(BASE_PATH.joinpath("log")) + "\\"
        if subdir:
            log_dir = log_dir + subdir + "\\"
    elif current_system == 'Linux':
        log_dir = "/var/log/NetCentric_log/"
        if subdir:
            log_dir = log_dir + subdir + "/"
    else:
        raise ValueError("System not supported. please check utils.path.get_log_file_dir.")

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    return log_dir


BASE_PATH = Path(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SRC_PATH = BASE_PATH.joinpath("src")
LOG_PATH = Path(get_log_file_dir())
# DATASET_PATH = BASE_PATH.joinpath("data_set")
