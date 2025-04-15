FROM python:3.13.3-slim-bookworm

RUN apt-get update && apt-get upgrade --yes
RUN apt-get install wget --yes

RUN useradd --create-home jan
USER jan
WORKDIR /home/jan

ENV VIRTUALENV=/home/jan/venv
RUN python3 -m venv $VIRTUALENV
ENV PATH="$VIRTUALENV/bin:$PATH"

COPY --chown=jan pyproject.toml ./
COPY --chown=jan README.md ./

RUN python -m pip install poetry 


COPY --chown=jan src/ src/
COPY --chown=jan tests/ tests/

RUN poetry install


# TODO: activate those lines again
RUN poetry run python -m pytest tests/
# RUN poetry run python -m pylint src/ --disable=C0114,C0116,R1705

CMD ["poetry", "run", "flask", "--app", "doro.app", "run", "--host", "0.0.0.0", "--port", "5000"]
# TODO try to run waitress or gunicorn instead of the flask buildin server
