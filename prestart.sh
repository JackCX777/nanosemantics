#! /usr/bin/env bash

sleep 30;
python ./nanosemantics_web_service/init_db.py
sleep 30;
python ./nanosemantics_web_service/main.py