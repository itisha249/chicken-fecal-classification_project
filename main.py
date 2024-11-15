from cnn_classifier import logger
from cnn_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipline
from cnn_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainigPipeline


logger.info("welcome to my custom log")


STAGE_NAME = "data ingestion stage"


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataIngestionTrainingPipline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx===========x")
        
    except Exception  as e:
        logger.exception(e)
        raise e
    



        STAGE_NAME ="preapre base model"
    try:
        logger.info(f"#*#*#*#*#*#*#*#*#*#*#*#*#")
        logger.info(f">>>>>>>>>> stage{STAGE_NAME} started <<<<<<<")
        prepare_base_model = PrepareBaseModelTrainigPipeline()
        prepare_base_model.main()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} complet <<<<<<<<<<\n\n========== x")
    except Exception as e:
        logger.exception(e)
        raise e