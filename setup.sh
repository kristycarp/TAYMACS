#!/bin/bash

echo "export TAYMACS_PATH=$PWD" >> ~/.bashrc
echo "alias taymacs=\"python \$TAYMACS_PATH/taymacs.py gmx\"" >> ~/.bashrc
source ~/.bashrc
