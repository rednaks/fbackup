Install :
========

Requirements :
-------------

Ensure you have `python-pip` and `python-virtualenv` installed on your computer

Installing dependencies :
-------------------------

    cd fbackup
    virtualenv .
    source bin/activate
    pip install -r requirements.txt

Running :
========

To backup a discussion run :

    ./fbackup access_token message_id
