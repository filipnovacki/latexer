import jinja2


class Compositor:
    def __init__(self, args):
        env = jinja2.Environment()
        self.latex_code = env.from_string('''
\\documentclass[{{font_size}}, a4paper]{ {{doc_type}} }
\\usepackage[utf8]{inputenc}
\\usepackage[ {{language}} ]{babel}
%TODO: more usepackages through loop
\\title{ {{title_name}} }

\\begin{document}
\\maketitle
\\tableofcontents



\\end{document}
 
''')

        args = vars(args)

        self.latex_code = self.latex_code.render(
            language=args['language'],
            title_name=args['title'],
            font_size=str(args['font_size']) + 'pt',
            doc_type=args['doc_type']
        )

        self.print_latex()

    def print_latex(self):
        print(self.latex_code)

    def __str__(self):
        return 'LaTeX document called ' + self.title.lstrip('\\title{').rstrip('}')
