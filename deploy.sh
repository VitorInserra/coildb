#!/bin/bash

oc new-app python:3.10~https://github.com/VitorInserra/coildb#main --context-dir=backend --strategy=docker
