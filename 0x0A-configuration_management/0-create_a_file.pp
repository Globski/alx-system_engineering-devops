# Create a file at /tmp/school with specified permissions, owner, group, and content.

file { 'school':
  ensure  => 'file',
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  path    => '/tmp/school',
}

