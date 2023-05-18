# increase nginx request limit

exec { 'nginx-fix':
  command => 'sed -i "s/15/22000/g" /etc/default/nginx',
  path    => '/bin/'
}

exec { 'restart nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
