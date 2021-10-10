#!/usr/bin/python3
""" takes an arg of two strings"""

from sys import argv, stderr
from os import path

def parse_header(header: list):
    """
    parse markdown header and convert to HTML
    """
    html = []

    for headertag in header:
        if len(headertag) > 0 and headertag[0] == '#':
            hashes = 0
            while hashes < len(
                    headertag) and headertag[hashes] == '#':
                hashes += 1
            if hashes > 6:
                hashes = 6
            html_h = 'h' + str(hashes)
            headertag = headertag.strip('#')
            headertag = headertag.strip(' ')
            headertag = '<' + html_h + '>' + headertag + '</' + html_h + '>'
        html.append(headertag)
    return html

def parse_ol(li: list):
    """
    parses markdown of ordered lists into html
    """

    html = []
    ul = False

    for uls in li:
        if len(uls) > 0 and uls[0] == '-':
            if ul:
                html.append('<li>' +uls[1:].lstrip(' ') + '</li>')
            else:
                ul = True
                html.append('<ul>')
                html.append('<li>' + uls[1:].lstrip(' ') + '</li>')
        elif (len(uls) == 0 or uls[0] != '-') and ul:
            ul = False
            html.append('</ul>')
            html.append(uls)
        else:
            html.append(uls)
        return html

if __name__=='__main__':
    def readIt():
        """ main function """
    
    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=stderr)
        exit(1)
    
    if path.exists(argv[1]) == False:
        print("Missing {}".format(argv[1]), file=stderr)
        exit(1)
    
    markdown = argv[1]
    output = argv[2]

    markdown_list = []


    with open(markdown, 'r') as f:
        markdown_list = f.read()
        markdown_list = ''.join(markdown_list).split('\n')
    
    markdown_list = parse_header(markdown_list)
    markdown_list = '\n'.join(markdown_list).split('\n')

    with open(output, 'w') as f:
        for markdown_h in markdown_list:
            f.write(markdown_h + '\n')