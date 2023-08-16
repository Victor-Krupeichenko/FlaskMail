#!/bin/bash

celery -A tasks.settings_celery:app_celery flower