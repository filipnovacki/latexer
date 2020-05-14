#!/usr/bin/env python
# This script generater LaTeX files

import argparse
from Compositor import Compositor

parser = argparse.ArgumentParser(description='Creates empty LaTeX document.')
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

args = parser.parse_args()
comp = Compositor(args)

