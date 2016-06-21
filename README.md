# PyPlanner
python commandline tool for saving events encrypted

PyPlanner encrypts the content of your calendar using AES-CBC encryption.
Your password will not be saved anywhere and is a SHA256 hash while runtime.
!!!If you lost your password ther is no option to recover your calendar!!!

Prerequisites:
- python27 (not tested with other versions)
- PyCrypto (get the latest version here: https://www.dlitz.net/software/pycrypto/)

what is working v1.1.0:
- add a new event
- create different calendars
- add a new event to specific calendar
- search by string
- search by date
- show calendars
- show events from specific calendar
- show next upcoming event
- show events in selected timeframe
- delete calendar
- delete event
- show year/month calendar
- help
- change password
- quit PyPlanner


ToDo:
- build an installer
- bugfixes
- performance improvements
- UX improvements
- search events by date
- show next upcoming event



