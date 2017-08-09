django-highlander
=================

There can be only one!

This is a Django `manage.py` Command class for long running tasks stated from crontab.

This uses posix semaphores to assure there is only one instance running at any time, so crontab will not start another
task unless the previous one finished.




