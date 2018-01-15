#!/usr/bin/env bash

apt-get update
apt-get -y upgrade
apt-get install -y python3-pip
apt-get install build-essential libssl-dev libffi-dev python-dev
pip3 install scrapy
pip3 install service_identity