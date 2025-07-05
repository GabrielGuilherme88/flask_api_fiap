import logging
import joblib

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
if not logger.handlers:
    logger.addHandler(handler)

model = joblib.load("iris_model.pkl")
logger.info("Modelo carregado com sucesso.")