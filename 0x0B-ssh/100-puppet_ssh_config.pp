# configuration to connect to a server without typing a password
file_line { 'disable password login':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
file_line { 'add path':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}
