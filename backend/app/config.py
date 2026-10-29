# config.py
# Loads and manages application configuration settings, including environment variables.

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  # Defines the default PostgreSQL connection URL for local development.
  # This can be overridden by setting DATABASE_URL in the environment or .env file.
  database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/internship_platform"

  # Configures how application settings are loaded.
  model_config = SettingsConfigDict(
    env_file=".env", # Loads environment variables from the .env file.
    extra="ignore", # Ignores additional environment variables not defined here.
  )

# Creates a settings instance that other application modules can import and use.
settings = Settings()