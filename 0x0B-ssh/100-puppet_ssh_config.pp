# Puppet manifest to configure SSH client
file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => template('ssh/ssh_config.erb'),
}

file_line { 'Turn off password authentication':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^#PasswordAuthentication',
}

file_line { 'Use the private key':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^#IdentityFile',
}

file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => template('ssh/ssh_config.erb'),
}

file { '/home/ubuntu/.ssh/school':
  ensure => 'present',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
  source => 'puppet:///modules/ssh/school',
}

file { '/home/ubuntu/.ssh/school.pub':
  ensure => 'present',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0644',
  source => 'puppet:///modules/ssh/school.pub',
}
