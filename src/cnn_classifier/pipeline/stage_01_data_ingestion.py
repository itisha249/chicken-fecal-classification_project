from cnn_classifier.config.configration import configurationManager
from cnn_classifier.components.data_ingetion import DataIngestion
from cnn_classifier import logger


STAGE_NAME = "data ingestion stage"


class DataIngestionTrainingPipline:
    def __init__(self):
        pass

    def main(self):
        config = configurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataIngestionTrainingPipline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx===========x")
    except Exception  as e:
        logger.exception(e)
        raise e