# on line: 137 require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );

exec { 'fix website':
  command => "sed -i 's/phpp/php/g' var/www/html/wp-settings.php",
  path    => '/usr/bin/env'
}
