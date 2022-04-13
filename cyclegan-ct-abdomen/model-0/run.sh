#!/bin/bash
echo $@

cd /cvib2/apps/personal/swelland/sandbox/gan/nn/cyclegan-ct-abdomen/model-0
CUDA_VISIBLE_DEVICES=2 python cyclegan_resnet.py
