# fixing LAMP stack website and typos

exec { 'fix website':
  path    => '/usr/bin/env'
  command => 'sed -i s/phpp/php/g var/www/html/wp-settings.php',
}
