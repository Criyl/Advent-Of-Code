ARG PYTHON_VERSION="3.11"


FROM python:${PYTHON_VERSION}-slim-buster AS base

FROM base AS poetry-install
RUN python3 -m ensurepip
RUN python3 -m pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export --with dev --without-hashes --format=requirements.txt > requirements.txt
RUN python3 -m pip install --user --ignore-installed -r requirements.txt

FROM base AS runner
COPY --from=poetry-install /root/.local /usr/local