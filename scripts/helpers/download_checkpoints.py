import sys

sys.path.insert(0, ".")
import os

from python_package_template.utils.config import cfg
from python_package_template.utils.downloader import download_from_GDrive
from python_package_template.utils.logger import Logger

cfg = cfg()
logger = Logger().logger


def download_checkpoints(list_checkpoints):
    for checkpoints in list_checkpoints:
        if not os.path.exists(checkpoints.path_local):
            download_from_GDrive(file_id=checkpoints.file_id, path_local=checkpoints.path_local)
        else:
            logger.warning(f"{checkpoints.path_local} already exist!")


if __name__ == "__main__":
    list_checkpoints = [cfg.checkpoints.model1, cfg.checkpoints.model2]
    download_checkpoints(list_checkpoints)
