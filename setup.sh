#!/bin/sh
CURRENT_DIR="$(cd "$(dirname "${0}")" && pwd)"

set -x

COMPOSE_FILE="${1:-docker-compose.yml}"
COMPOSE_FILE="${CURRENT_DIR}/${COMPOSE_FILE}"

cd "${CURRENT_DIR}"

sudo rm -rf "${CURRENT_DIR}/tests/__pycache__/"
sudo rm -rf "${CURRENT_DIR}/.tox"

docker-compose -f "${COMPOSE_FILE}" up --build
