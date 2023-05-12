# fixing LAMP stack website and typos

exec { '/usr/local/bin/:bin sed -i "s/phpp/php/g" var/www/html/wp-settings.php': }
