from imapclient import IMAPClient
from taskw import TaskWarrior
import email
from email.header import Header, decode_header, make_header

server=IMAPClient("imapserver.yo")
server.login('login', 'pass')
server.select_folder("INBOX")
messages = server.search("FLAGGED")
w=TaskWarrior()
tsk=w.filter_tasks({'tag':'email'})
clean=[]
for uid, message_data in server.fetch(messages, "RFC822").items():
    n=next((item for item in tsk if 'mailid' in item and item['mailid'] == str(uid)), False)
    if n==False:
        email_message = email.message_from_bytes(message_data[b"RFC822"])
        if email_message.get("Subject") is not None:
            w.task_add(repr(str(make_header(decode_header(email_message.get("From")))))+" "+repr(str(make_header(decode_header(email_message.get("Subject"))))),tag="email", mailid=uid)
    else:
        if n['status']=='completed':
           clean.append(uid)
server.remove_flags(clean, "\\Flagged")

