import os
import sys

import thread
import xml.extree.ElementTree as etree

def writeToFile(prts, msgs):
    if len(prts) == 0:
        print('There is no participants in a thread, currently being skipped!');
        args = '' #need to make sure that this is going to be properly defined
    output = os.path.join(args.outdir, ', '.join(prts) + '.html')

        if not os.path.exists(output):
            print('Appending: ', output)
            handle = open(output, 'w+')
            handle.write(''
                         '<!DOCTYPE html>'
                         '<meta http-equiv="Content-Type" content="text/html"; charset=utf-8>')
            handle.write('<style type="text/css>'
                         'body {'
                         'font-family: sans-serif;'
                                                
                         '}'
                         '.user {'
                         'font-weight: bold;'
                         '}'
                         '.meta {'
                         'margin-left: lem;'
                         'color:#999'
                         '}'
                          '</style>')
            handle.write('<p> Participants: >> ' + (','.join(prts)) + '</p>')

        elif os.path.isfile(output):
            print('Writing to file >> ', output)
            handle = open(output, 'a+')

            for (header, body) in msgs:
                handle.write(header)
                handle.write(body)
                handle.write('<hr>')
                handle.close()

def processFile(action = writeToFile()):
    args = '' #need to make sure that this is going to be properly defined
    msgs = []
    prts = []
    savedHead = savedBody = None

    for elem in thread.getChildren():
        if elem.tag == 'div':
            prts = elem.find('./div/span')
            if prts != None and prts.text != None:
                if not prts.text in prts and not prts.text == args.name:
                    prts.append(prts.text)
         savedHead = etree.toString(elem, encoding='unicode')
