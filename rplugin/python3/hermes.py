#!/usr/bin/python3
# -*- coding: utf-8 -*-
from subprocess import call
from os.path import expanduser
class Hermes(object):

    """Hermes is the main class. All configuration goes into it"""
    #members
    fetch_protocol = str() #Either imap, pop3, maildir or mailbox
    send_protocol = str()  #Either smtp or cmd
    fetch_source = str()   #Either server:port or /path/to/maildir\/mailbox
    send_source = str()    #Either command or server:port
    head_file = str()      #Where all headers will be stored
    destroy_on_end = False #If true, destroys head_file
    def __init__(self, send_protocol, fetch_protocol, source_fetch,source_send):
        """TODO: to be defined1. """
        self.fetch_protocol = fetch_protocol
        self.send_protocol = send_protocol
        self.fetch_source = source_fetch
        self.send_source = source_send

    def get_fetch_protocol(self):
        return self.fetch_protocol
    def get_send_protocol(self):
        return self.send_protocol
    def get_fetch_source(self):
        return self.fetch_source
    def get_send_source(self):
        return self.send_source
    def sync_to_header_file():
        """Syncs messages to header file"""
