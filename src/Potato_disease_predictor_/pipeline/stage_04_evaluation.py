from Potato_disease_predictor_.config.configuration import ConfigurationManager
from Potato_disease_predictor_.components.evaluation import Evalution
from Potato_disease_predictor_ import logger



STAGE_NAME="Evalution stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config=config.get_validation_config()
        evalution = Evalution(val_config)
        evalution.evalution()
        evalution.save_score()



if __name__=="__main__":
    try:
        logger.info(f"********************")
        logger.info(f">>>>>>>>>>stage {STAGE_NAME} started<<<<<<<<")
        obj=EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME}  completed <<<<<<<<<\n\nx==============x")
    except Exception as e:
        raise e
        

  
              