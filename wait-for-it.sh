#!/usr/bin/env bash
set -e

TIMEOUT=15
HOST=db
PORT=5432

echo "Waiting for $HOST:$PORT..."

for i in `seq $TIMEOUT` ; do
    nc -z $HOST $PORT && break
    echo "Waiting for $HOST:$PORT... retrying ($i/$TIMEOUT)"
    sleep 1
done

if [ $i -eq $TIMEOUT ]; then
    echo "Error: Timed out waiting for $HOST:$PORT" >&2
    exit 1
fi

echo "$HOST:$PORT is ready!"
exec "${@:3}"
