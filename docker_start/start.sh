#!/bin/bash

echo "Waiting..."
sleep 5
alembic upgrade head
echo "FINISH UPGRADE.."
celery -A tasks.tasks worker -l info &
gunicorn app:app --bind=0.0.0.0:5000
