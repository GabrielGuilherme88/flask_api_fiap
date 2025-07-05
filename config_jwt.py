import logging

JWT_SECRET = "MEUSEGREDOAQUI"
JWT_ALGORITHM = "HS256"
JWT_EXP_DELTA_SECONDS = 3600

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("main")