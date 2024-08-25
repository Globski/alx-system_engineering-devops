# Increases the amount of traffic an Nginx server can handle.
# Increase the ULIMIT of the default file from 15 to 4096
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/bin/:/bin/'
}

# Restart Nginx
exec { 'restart-nginx':
  command => '/usr/sbin/service nginx restart'
}
