#!/bin/bash

# start up the Ruby application and listen to port 9292
cd /var/www/simple-sinatra-app/
/usr/local/bin/bundle exec rackup -p 9292 >/dev/null 2>&1 &
#sleep 20
