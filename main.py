from Potato_disease_predictor_ import logger
from Potato_disease_predictor_.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Potato_disease_predictor_.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from Potato_disease_predictor_.pipeline.stage_03_training import ModelTrainingPipeline 
from Potato_disease_predictor_.pipeline.stage_04_evaluation import EvaluationPipeline
STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========x")
except Exception as e:
    raise e  



STAGE_NAME="Prepare base MOdel"

try:
        logger.info(f"******************")
        logger.info(f">>>>>>stage {STAGE_NAME} started <<<<<<<")
        prepare_base_model=PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>>stage {STAGE_NAME} completed <<<<<<<\n\nx============x")


except Exception as e:
    raise e



STAGE_NAME="Training"


try:
        logger.info(f"*****************")
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        model_trainer=ModelTrainingPipeline()
        model_trainer.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME}  completed <<<<<<<<\n\nx===========x")

except Exception as e:
    raise e


STAGE_NAME="Evaluation stage"

try:
        logger.info(f"********************")
        logger.info(f">>>>>>>>>>stage {STAGE_NAME} started<<<<<<<<")
        obj=EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME}  completed <<<<<<<<<\n\nx==============x")
except Exception as e:
        raise e