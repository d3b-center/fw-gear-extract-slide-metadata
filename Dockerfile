FROM flywheel/python:main.a30a2597 AS deps

ENV FLYWHEEL="/flywheel/v0"
WORKDIR ${FLYWHEEL}

# Install main deps
COPY pyproject.toml poetry.lock $FLYWHEEL/
RUN poetry install --no-dev --no-root

COPY run.py manifest.json README.md $FLYWHEEL/
COPY fw_gear_extract_slide_metadata ${FLYWHEEL}/fw_gear_extract_slide_metadata 

# Installing the current project (most likely to change, above install is cached)
RUN poetry install --no-dev

# Configure entrypoint
RUN chmod a+x $FLYWHEEL/run.py
ENTRYPOINT ["poetry","run","python","/flywheel/v0/run.py"]
