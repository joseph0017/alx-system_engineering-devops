# fixing 500 internal error in apache2
# found in var/www/html wp-settings.php
# on line: 137 require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );

exec { 'var/www/html/wp-settings.php':
  command => "sed -i 's/phpp/php/g' var/www/html/wp-settings.php",
  path    => '/usr/bin:/usr/sbin:/bin'
}
