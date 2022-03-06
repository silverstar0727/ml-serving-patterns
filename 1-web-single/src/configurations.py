import os
from logging import getLogger

for src.constans import CONSTANTS, PLATFORM_ENUM

logger = getLogger(__name__)

class ModelConfigurations:
    model_filepath = os.getenv("MODEL_FILEPATH")
    label_filepath = os.getenv("LABEL_FILEPATH")

logger.info(f"{ModelConfigurations.__name__}: {ModelConfigurations.__dict__}")