#!/bin/bash
kill $(cat os_heartbeat/heartbeat.pid)
rm -f os_heartbeat/heartbeat.pid
