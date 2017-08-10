django-highlander
=================

There can be only one!

This is a Django `manage.py` Command class for long running tasks started from crontab.

One problem with this kind of task is that crontab may start other instances before the previous one finishes, and if this happens a lot you will end up with too many processes running simultaneously which can make a server halt.

Using this as the base class instead of BaseCommand will assure there is only one instance running at any time, and second instance will not run unless the previous one finished.

Install
-------

Just grab it from the cheese shop:

    pip install django-highlander


How to use
----------

Just inherit from Highlander instead of BaseCommand:

    from djangohighlander.command import Highlander

    class Command(Highlander):
        def handle(self, *args, **options):
            ...


