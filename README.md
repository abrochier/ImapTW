# ImapTW
A quick and dirty script to synchronize taskwarrior and an IMAP mailbox. This only does two things:
* Every email that is flagged (or starred, or however it appears in your mailbox) is turned into a task, with the tag `email` and as descripition the sender(s) and the subject of the email.
* Once the tasked is marked as done in TW, the corresponding mail is unflagged.
* The opposite is not true: unflagging an email do not mark the corresponding task as done. Once the task is created it makes sense to me that this should be handled directly in TW.

# Install 

Make sure you have Imapclient and taskw installed
```shell 
pip install imapclient taswk
```
Create a user defined attributes for TW called mailid

```shell
task config uda.mailid.type string
```

Download and edit the file `imaptw.py`, change login and password to the correct thing. Setup your cron to execute this script as often as you like.

# License
Public domain.
