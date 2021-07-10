#!/bin/bash

monero-wallet-rpc --daemon-login ralston:password --daemon-address 127.0.0.1:18081  --rpc-login ralston:password --rpc-bind-ip 127.0.0.1 --rpc-bind-port 18083 --wallet-file /Users/ralston/xmrpy.keys --prompt-for-password --trusted-daemon --log-level 4