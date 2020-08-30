#!/bin/sh

set -xe

USER_ID=${UID}
GROUP_ID=${GID}

if [ ! -f "/app/db/db.sqlite3" ]; then
    python3 ./manage.py migrate
else
    python3 ./manage.py migrate
    python3 ./manage.py importlang
fi

echo "Setting permissions to UID/GID: ${USER_ID}/${GROUP_ID}"
chown ${USER_ID}:${GROUP_ID} -R /app

exec su-exec ${USER_ID}:${GROUP_ID} "$@"