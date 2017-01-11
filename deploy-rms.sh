#!/bin/sh

echo "=========================================="
echo "==> start to upload rms to Github..."

git status;
git add .;

arg1="$1"
git commit -m "$arg1";
git push origin master;

echo "==> start to deploy rms to heroku..."
git push heroku master;
heroku run python manage.py makemigrations;
heroku run python manage.py migrate;

echo "==> [done] start to deploy rms to heroku..."
heroku ps:scale web=1;
heroku open;



