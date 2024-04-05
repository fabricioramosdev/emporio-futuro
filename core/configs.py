from pydantic import BaseSettings

class Settings(BaseSettings):
    API_PREFIX: str = '/api/v2'
    API_TITLE: str = 'Empório do Futuro'
    API_VERSION: str =  '0.1.10'
    API_DESCRIPTION: str = 'Api do empório do futuro'

    ACCESS_TOKEN_EXPIRE_MIN = 60
    REFLESH_TOKEN_EXPIRE_MIN = 60 * 24 * 7
    ALGORITHM = 'HS256'

    DB_URL = 'postgresql+asyncpg://udsi255l6s28mh:p1322b823585610f6af4a92c8fd930549dac33496380b4c239b9a8cd781761f98@c7gljno857ucsl.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/ddtsbc7fjh6kje'


    class Config:
        case_sensitive = True


settings = Settings()


