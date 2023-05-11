# Isuue summary
In the software engineering program by ALX, we were assigned to find the root cause of a 500 Internal service error.
A 500 error indicates that there is an error on the server-side i.e the website's server. So something must be wrong on 
the website's server. The website was running on a LAMP (Linux, Apache, MySql, PHP) stack. This error affected the users,
well because you can't access the website unless the 500 error has been resolved. I sought out to investigate the cause of this error.

# Timeline
* 10/05/23 8:13PM (GMT+1) The process of debugging begins
* 10/05/23 8:25PM (GMT+1) Made a http request to the server, got back a 500 error response.
* 10/05/23 9:11AM (GMT+1) using strace and netstat, I confirmed that the Apache2 and MySql are running.
* 10/05/23 12:19AM (GMT+1) checked the configurations files for MySQL, Apache2, and indeed they are valid. Yet Apache2 fails.
* 10/05/23 2:45AM (GMT+1)  checked the var/logs no logs for PHP found.
* 10/05/23 3:00AM (GMT+1) checked the configuration files for PHP in /var/www/html/wp-settings.php
found the error "on line: 137 require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );"

# Root cause and resolution
The error was a mispelling error on line 137 "require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );" it should be "require_once( ABSPATH . WPINC . '/class-wp-locale.php' )".
The error was corrected by writing a puppet script that fixed all mispelling errors in the PHP configuration file.

# Corrective and preventative measures
After setting up configuration files, the application must be tested to ensure all is working properly. Mispelling happens even to the most experienced programmers,
for this I recommend installing extensions on IDEs to prevent mispelling. There are various extensions, which make writing code easier and faster, and certainly,
prevent things such as mispelling.
Lastly checking the configuration files is a good way to go, and to follow the debugging process as mentioned above.
