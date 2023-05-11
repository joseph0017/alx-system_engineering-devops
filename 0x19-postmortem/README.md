# Isuue Summary
In the software engineering program by ALX, we were assigned to find the root cause of a 500 Internal service error.
A 500 error indicates that there is an error on the server-side i.e the website's server. So something must be wrong on 
the website's server. The website was running on a LAMP (Linux, Apache, MySql, PHP) stack. This error affected the users,
well because you can't access the website unless the 500 error has been resolved. I sought out to investigate the cause of this error.

# Timeline
10/05/23 8:13PM (GMT+1) The process of debugging begins
10/05/23 8:25PM (GMT+1) Made a http request to the server, got back a 500 error response.
10/05/23 9:11AM (GMT+1) using strace and netstat, I confirmed that the Apache2 and MySql are running
10/05/23 12:19AM (GMT+1) checked the configurations files for MySQL, Apache2
