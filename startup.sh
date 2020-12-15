#!/bin/bash
export DATABSE_URI="mysql+pymysql://root:1234@34.105.208.208/todolsit"
export SECRET_KEY="AOSEDUIRFGHLIUADSBV"
cd /opt/todo-list-app
sudo python3 -m venv venv
source venv/bin/activate
pip3 install -r requiremnets.txt
python3 app.py 