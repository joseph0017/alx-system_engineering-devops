# on line: 137 require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );

exec { 'var/www/html/wp-settings.php':
  command => "sed -i 's/phpp/php/g' var/www/html/wp-settings.php",
  path    => '/bin'
}
