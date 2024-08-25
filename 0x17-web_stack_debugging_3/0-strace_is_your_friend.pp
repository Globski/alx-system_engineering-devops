# Puppet code to resolve a 5xx error on a WordPress site by correcting a typo in the wp-settings.php file.
# Specifically, it replaces "phpp" with "php", which may be causing the server to return a 500 Internal Server Error.
exec { 'fix-wordpress-error':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/bin/:/bin/'
}
