FROM python:3.9.7-slim-buster

ENV FLYWHEEL="/flywheel/v0"
WORKDIR ${FLYWHEEL}

RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean

RUN apt-get install openslide-tools --yes
RUN apt-get install python-openslide --yes

# Install main deps
RUN pip install poetry
COPY pyproject.toml poetry.lock $FLYWHEEL/
RUN poetry install --no-root

COPY run.py manifest.json README.md $FLYWHEEL/
COPY fw_gear_extract_slide_metadata ${FLYWHEEL}/fw_gear_extract_slide_metadata 

# Installing the current project (most likely to change, above install is cached)
RUN poetry install

# Configure entrypoint
RUN chmod a+x $FLYWHEEL/run.py
ENTRYPOINT ["poetry","run","python","/flywheel/v0/run.py"]
