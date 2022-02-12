#!/usr/bin/sh

echo "Installing python virtual environment..."
python3 -m pip install virtualenv

echo "Creating virtual environment..."
python3 -m virtualenv env

echo "Switching to env..."
source env//bin//activate

echo "Installing requirements..."
python -m pip install -r requirements.txt

echo "Up server..."
python src//app.py
