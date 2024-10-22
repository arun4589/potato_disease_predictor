import os
import urllib.request as request
import zipfile
from Potato_disease_predictor_ import logger
from Potato_disease_predictor_.utils.common import get_size
from Potato_disease_predictor_.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(url=self.config.source_URL,
                                                   filename=self.config.local_data_file)
            logger.info(f"{filename} download! with following info :\n{headers}")

        else:
            
            logger.info(f"file already exist of size : {get_size(Path(self.config.local_data_file))}")



    def extract_zip_file(self):
        
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        
        try:
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
               zip_ref.extractall(unzip_path)
        except zipfile.BadZipFile:
          print(f"Error: The file '{self.config.local_data_file}' is not a valid ZIP file or is corrupted.")
        except FileNotFoundError:
          print(f"Error: The file '{self.config.local_data_file}' does not exist.")
            



