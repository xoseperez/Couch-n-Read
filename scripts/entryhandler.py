# coding=UTF-8
import xml.sax.handler
 
class EntryHandler(xml.sax.handler.ContentHandler):
    '''
    SAX Parser for Tellico files.
    The main problem of this approach is that it gathers all the 
    information first. A better way whould be to store the books
    in the DB while reading the XML file.
    '''

    # Tags to handle
    TAGS = ['title', 'isbn', 'publisher', 'theme', 'genre', 'cdu', 
        'location', 'comments', 'year', 'edition_year', 'pages', 'owner',
        'condition']
    # This tags represent a 1 to N relation form the book POW
    LIST_TAGS = ['author', 'language']

    def __init__(self):
        self.capture = False
        self.entries = []
        self.TAGS.extend(self.LIST_TAGS)
 
    def startElement(self, name, attributes):
        '''
        Starts an book entry or starts data capturing for given tags
        '''
        self.buffer = []
        if name == "entry":
            self.entry = {}
            self.entry['id'] = attributes["id"]
        elif name in self.TAGS:
            self.capture = True
 
    def characters(self, data):
        '''
        Captures the contents of a tag if this has been set to be captured
        '''
        if self.capture:
            self.buffer.append(data)
 
    def endElement(self, name):
        '''
        Stops tag campturing and handles data storage in a dictionary
        '''
        self.capture = False
        data = ''.join(self.buffer)
        if name == "entry":
            self.entries.append(self.entry)
        elif name in self.LIST_TAGS:
            if self.entry.has_key(name):    
                self.entry[name].append(data)
            else:
                self.entry[name] = [data]
        elif name in self.TAGS:
            self.entry[name] = data



