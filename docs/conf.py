#!/usr/bin/env python3
# coding: utf-8

import os
import re
import sys

from sphinx.ext import autodoc

sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir))

extensions = [
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = 'Graphite-API'
copyright = u'2014, Bruno Renié'

version = '1.0'
release = '1.0'

exclude_patterns = ['_build']

pygments_style = 'sphinx'

html_theme = 'default'

htmlhelp_basename = 'Graphite-APIdoc'

latex_elements = {
}

latex_documents = [
    ('index', 'Graphite-API.tex', 'Graphite-API Documentation',
     'Bruno Renié', 'manual'),
]

man_pages = [
    ('index', 'graphite-api', 'Graphite-API Documentation',
     ['Bruno Renié'], 1)
]

texinfo_documents = [
    ('index', 'Graphite-API', 'Graphite-API Documentation',
     'Bruno Renié', 'Graphite-API', 'One line description of project.',
     'Miscellaneous'),
]


class RenderFunctionDocumenter(autodoc.FunctionDocumenter):
    priority = 10

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        return autodoc.FunctionDocumenter.can_document_member(
            member, membername, isattr, parent
        ) and parent.name == 'graphite_api.functions'

    def format_args(self):
        args = super(RenderFunctionDocumenter, self).format_args()
        if args is not None:
            return re.sub('requestContext, ', '', args)


def setup(app):
    app.add_autodocumenter(RenderFunctionDocumenter)

add_module_names = False