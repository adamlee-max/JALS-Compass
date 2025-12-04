#!/bin/bash
nohup python3 os_heartbeat/daemon.py &
echo $! > os_heartbeat/heartbeat.pid
