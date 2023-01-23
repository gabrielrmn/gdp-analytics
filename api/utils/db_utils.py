from sqlalchemy import create_engine
import settings as config


def get_engine():
    con_str = 'postgresql://{}:{}@{}:{}/{}'.format(
        config.DB_USER, config.DB_PASS, config.DB_HOST, config.DB_PORT, config.DB_NAME)
    engine = create_engine(
        con_str)
    return engine
