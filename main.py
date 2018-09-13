#!/usr/bin/env python
# This script generater LaTeX files

import argparse
import sys
from Logic.Compositor import Compositor

parser = argparse.ArgumentParser(description='Start a LaTeX file. Allows a lot of default customization'
                                             'by using arguments. The defaults are set to suit my needs. '
                                             'I only tested it for articles, books, reoprts and similiar '
                                             'documents. Beamer might come some day')
parser.add_argument('-fs',
                    '--font_size',
                    type=int,
                    metavar='',
                    help='font size used for document (10, 11 or 12)',
                    default=11)

parser.add_argument('-ft',
                    '--font_type',
                    default=None,
                    metavar='',
                    help='The font in which the document will be typeset in')

parser.add_argument('-dt',
                    '--doc_type',
                    metavar='',
                    default='article',
                    help='Type of paper to make (article, book, report...)')

parser.add_argument('-lang',
                    '--language',
                    metavar='',
                    default='croatian',
                    help='Language of the LaTeX docuement that will be produced')

parser.add_argument('title',
                    help='Title of the paper')

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

# comp = Compositor()
args = parser.parse_args()
comp = Compositor(args)
# print(args)

# All data is saved in comp class instance
# print(comp.font_size)
# print(file_content)
