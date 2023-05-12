# fixing LAMP stack website and typos
exec { 'fix website':
  command => 'sed -i s/phpp/php/g var/www/html/wp-settings.php',
  path    => '/usr/bin/env'
}
