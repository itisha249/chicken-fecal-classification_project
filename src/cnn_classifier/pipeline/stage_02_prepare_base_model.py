from cnn_classifier.entity.config_manager import ConfigurationManager
from cnn_classifier.components.prpare_base_model import PrepareBasemodel
from cnn_classifier import logger



STAGE_NAME = "preapre base model"


class PrepareBaseModelTrainigPipeline:

    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        Prepare_base_model_config = config.get_prepare_base_model_config()
        Prepare_base_model = PrepareBasemodel(config=Prepare_base_model_config)
        Prepare_base_model.get_base_model()
        Prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f"#*#*#*#*#*#*#*#*#*#*#*#*#")
        logger.info(f">>>>>>>>>> stage{STAGE_NAME} started <<<<<<<")
        obj = PrepareBaseModelTrainigPipeline()
        obj.main()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} complet <<<<<<<<<<\n\n========== x")
    except Exception as e:
        logger.exception(e)
        raise e