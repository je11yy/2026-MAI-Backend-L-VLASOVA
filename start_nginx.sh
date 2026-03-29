#!/bin/bash
rm -f logs/*.log
nginx -p "$PWD" -c nginx.conf