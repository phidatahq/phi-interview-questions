from __future__ import annotations

from typing import Optional

from pydantic_settings import BaseSettings


class DbSettings(BaseSettings):
    """Database settings that can be set using environment variables.

    Reference: https://docs.pydantic.dev/latest/usage/pydantic_settings/
    """

    # Database configuration
    db_host: Optional[str] = None
    db_port: Optional[int] = None
    db_user: Optional[str] = None
    db_pass: Optional[str] = None
    db_database: Optional[str] = None
    db_driver: str = "postgresql+psycopg"
    # Create/Upgrade database on startup using alembic
    migrate_db: bool = False

    def get_db_url(self) -> str:
        url = "{}://{}{}@{}:{}/{}".format(
            self.db_driver,
            self.db_user,
            f":{self.db_pass}" if self.db_pass else "",
            self.db_host,
            self.db_port,
            self.db_database,
        )
        # Use local database if db_host is None
        if "None" in url:
            from os import getenv
            from dev_resources import dev_db

            if getenv("PHI_RUNTIME") is None:
                print("Using local connection")
                local_db_url = dev_db.get_db_connection_local()
                if local_db_url:
                    return local_db_url
            raise ValueError("Could not build database connection")
        return url


# Create DbSettings object
db_settings = DbSettings()
