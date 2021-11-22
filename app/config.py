from pydantic import BaseSettings

class CheckEnvironVariables(BaseSettings):
    """
    Check the env variables and throus error if the variable is not available
    """
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        """setting the env_file will assign the values from the file to the environment variables mentioned above"""
        env_file = ".env"

settings = CheckEnvironVariables()