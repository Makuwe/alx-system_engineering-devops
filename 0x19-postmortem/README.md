My first postmortem Report

Diagnosing and Resolving Apache 500 Error with strace and Puppet Automation
Issue Summary:
On August 15, 2024, at approximately 10:00 AM GMT, our monitoring systems alerted us to recurring HTTP 500 Internal Server Error responses from the Apache web server running on our production environment. This incident led to service disruption for our users, prompting an immediate investigation. 89 % of the users were affected.
Timeline:
10:00 AM GMT: Initial alert received regarding the 500 errors.
10:05 AM GMT: Investigation commenced using strace to analyze Apache processes.
10:20 AM GMT: Identified the root cause of the error.
10:30 AM GMT: Implemented a fix to the Apache configuration.
10:45 AM GMT: Confirmed the resolution of the issue; Apache returned to normal operation.
11:00 AM GMT: Started the process of automating the fix using Puppet.
Root cause and resolution
The wp-settings.php file's incorrect file name reference was the root of the problem. The server responded with an error code of 500 when the attempt to curl the server was made. It was discovered through reviewing the error logs that no error log file was being written for PHP failures, and there was little information about the server's premature shutdown to be obtained in reading the default error log for Apache.
Then checking the phpp file's error log settings after realizing that the php errors were not being sent anywhere and discovered that all error logging had been enabled, the Apache server's error logging was restarted to see if any issues were showing up in the log. The php log confirmed what was expected: the wp-settings.php file did not contain a file with the.phpp extension. This was obviously a typographical error that caused the site access error. Since the issue was only discovered in one server, it's possible that it was also duplicated in other servers. Fixing the file extension with puppet would be a simple solution that would also affect other servers.
Corrective and preventative measures
Error logging should be enabled on all servers and websites in order to quickly discover problems in the event that they arise.
Before deploying on a multi-server setup, all servers and sites should be checked locally. This will allow for the correction of issues prior to being live, cutting down on the amount of time needed to fix a downed site.
Resource management: Constant observation and improvement.
Planning for Incident Response: Create and record a detailed plan.
