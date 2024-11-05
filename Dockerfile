FROM phidata/python:3.12

ARG APP_DIR=/app
ENV APP_DIR=${APP_DIR}
WORKDIR ${APP_DIR}

# Copy requirements.txt
COPY requirements.txt ./

# Install requirements
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip sync requirements.txt --system

# Copy project files
COPY . .

ENTRYPOINT ["/app/scripts/entrypoint.sh"]
CMD ["chill"]
