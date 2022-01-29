#!/bin/bash

LOG_FILE="$PWD/logs/minio.log"

export MINIO_ACCESS_KEY=minioadmin
export MINIO_SECRET_KEY=minioadmin

./minio server --address :9000 http://121.141.161.74/app/minio/sample/data http://121.141.161.242/app/minio/sample/data http://121.141.152.77/app/minio/sample/data http://121.141.148.145/app/minio/sample/data >> $LOG_FILE

MINIO_PID=$!

if [ ! -z $MINIO_PID ] ; then
     echo "$MINIO_PID" > minio.pid
fi
