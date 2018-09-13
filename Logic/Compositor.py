class Compositor:
    def __init__(self, args):
        self.other_data = '''
\\usepackage[utf8]{inputenc}

% Font:
% \\usepackage{palatino}
% \\usepackage{bookman}

        '''
        self.beginstart = '''
\\begin{document}
\\maketitle
\\tableofcontents
\\end{document}
        '''

        args = vars(args)
        self.doc_class = '\\documentclass[10pt, a4paper] {} '.format('{' + args['doc_type'] + '}')
        self.lang = '\\usepackage[{}'.format(args['language'] + ']{babel}')
        self.title = '\\title{}'.format('{' + args['title'] + '}')

        # print(self)
        self.print_latex()

    def print_latex(self):
        file = self.doc_class + \
               self.lang + \
               self.other_data + \
               self.title + \
               self.beginstart

        print(file)

    def __str__(self):
        return 'LaTeX document called ' + self.title.lstrip('\\title{').rstrip('}')
