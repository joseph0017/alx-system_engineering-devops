# creating a custom HTTP header response, but with Puppet

exec { 'apt-update':
  command => '/usr/bin/apt-get update'
}

package { 'nginx':
  ensure => 'installed',
  name   => 'nginx',
}

file_line { 'add header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By $HOSTNAME;",
  after  => 'server_name _;',
}

service { 'nginx':
  ensure => 'running',
}
