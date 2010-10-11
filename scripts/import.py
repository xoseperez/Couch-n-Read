# coding=UTF-8
# Python imports
import sys
import xml.sax
import json
from couchdb import Server

# Application imports
import entryhandler

DB_HOST = 'http://127.0.0.1:5984'
DB_NAME = 'tellico'

def load_database(entries):
    '''
    Loads entries data into database
    '''    

    # Open connection
    server = Server(DB_HOST)

    # Create a clean database
    if DB_NAME in server:
        del server[DB_NAME]
    db = server.create(DB_NAME)

    keys = []
    for entry in entries:
        db.create(json.dumps(entry))

def show_entries(entries):
    for entry in entries:
        print json.dumps(entry)
    
def import_tellico(tellico_file):
    '''
    Gets entries list from SAX Parser
    '''
    parser = xml.sax.make_parser()
    handler = entryhandler.EntryHandler()
    parser.setContentHandler(handler)
    parser.parse(tellico_file)
    return(handler.entries)

def main():
    '''
    Parses command line arguments and calls importer
    '''
    args = sys.argv[1:]
    if len(args) != 1:
        print 'Usage: python import.py <tellico_file>'
        sys.exit(-1)
    load_database(import_tellico(args[0]))
    #show_entries(import_tellico(args[0]))

if __name__ == '__main__':
    main()

