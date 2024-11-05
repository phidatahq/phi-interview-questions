from pathlib import Path

from phi.docker.app.fastapi import FastApi
from phi.docker.app.postgres import PostgresDb
from phi.docker.resources import DockerResources
from phi.docker.resource.image import DockerImage

key = "phi-interview-questions"
ws_root = Path(__file__).parent.resolve()

# -*- Dev image
dev_image = DockerImage(
    name="phidata/interview-questions",
    tag="dev",
    path=str(ws_root),
    # Set to True to build the image locally
    enabled=False,
)

# -*- Dev database running on port 5432
dev_db = PostgresDb(
    name=f"db-{key}",
    pg_user="phi",
    pg_password="phi",
    pg_database="phi",
    # Connect to this db on port 5432
    host_port=5432,
)

# -*- Dev API running on port 8000
dev_fastapi = FastApi(
    name=f"api-{key}",
    image=dev_image,
    command="uvicorn api.main:app --reload",
    port_number=8000,
    debug_mode=True,
    mount_workspace=True,
    env_vars={
        "RUNTIME_ENV": "dev",
        # Database configuration
        "DB_HOST": dev_db.get_db_host(),
        "DB_PORT": dev_db.get_db_port(),
        "DB_USER": dev_db.get_db_user(),
        "DB_PASS": dev_db.get_db_password(),
        "DB_DATABASE": dev_db.get_db_database(),
        # Wait for database to be available before starting the server
        "WAIT_FOR_DB": True,
        # Migrate database on startup using alembic
        "MIGRATE_DB": True,
    },
)

# -*- Define the dev resources running on docker
dev_resources = DockerResources(
    network=key,
    apps=[dev_db, dev_fastapi],
)
