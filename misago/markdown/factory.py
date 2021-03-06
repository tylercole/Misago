import re
import markdown
from HTMLParser import HTMLParser
from django.conf import settings
from django.utils.importlib import import_module
from django.utils.translation import ugettext_lazy as _
from misago.utils import get_random_string

class ClearHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.clean_text = ''
        self.lookback = []
        
    def handle_entityref(self, name):
        if name == 'gt':
            self.clean_text += '>'
        if name == 'lt':
            self.clean_text += '<'

    def handle_starttag(self, tag, attrs):
        self.lookback.append(tag)

    def handle_endtag(self, tag):
        try:
            if self.lookback[-1] == tag:
                self.lookback.pop()
        except IndexError:
            pass
        
    def handle_data(self, data):
        # String does not repeat itself
        if self.clean_text[-len(data):] != data:
            # String is not "QUOTE"
            try:
                if self.lookback[-1] in ('strong', 'em'):
                    self.clean_text += data
                elif not (data == 'Quote' and self.lookback[-1] == 'h3' and self.lookback[-2] == 'blockquote'):
                    self.clean_text += data
            except IndexError:
                self.clean_text += data


def clear_markdown(text):
    parser = ClearHTMLParser()
    parser.feed(text)
    return parser.clean_text


def remove_unsupported(md):
    # References are evil, we dont support them
    del md.preprocessors['reference']
    del md.inlinePatterns['reference']
    del md.inlinePatterns['image_reference']
    del md.inlinePatterns['short_reference']


def signature_markdown(acl, text):
    md = markdown.Markdown(
                           safe_mode='escape',
                           output_format=settings.OUTPUT_FORMAT,
                           extensions=['nl2br'])

    remove_unsupported(md)

    if not acl.usercp.allow_signature_links():
        del md.inlinePatterns['link']
        del md.inlinePatterns['autolink']
    if not acl.usercp.allow_signature_images():
        del md.inlinePatterns['image_link']

    del md.parser.blockprocessors['hashheader']
    del md.parser.blockprocessors['setextheader']
    del md.parser.blockprocessors['code']
    del md.parser.blockprocessors['quote']
    del md.parser.blockprocessors['hr']
    del md.parser.blockprocessors['olist']
    del md.parser.blockprocessors['ulist']
    
    return md.convert(text)


def post_markdown(request, text):
    md = markdown.Markdown(
                           safe_mode='escape',
                           output_format=settings.OUTPUT_FORMAT,
                           extensions=['nl2br', 'fenced_code'])

    remove_unsupported(md)
    md.mi_token = get_random_string(16)
    for extension in settings.MARKDOWN_EXTENSIONS:
        module = '.'.join(extension.split('.')[:-1])
        extension = extension.split('.')[-1]
        module = import_module(module)
        attr = getattr(module, extension)
        ext = attr()
        ext.extendMarkdown(md)
    text = md.convert(text)
    return tidy_markdown(md, text)


def tidy_markdown(md, text):
    text = text.replace('<p><h3><quotetitle>', '<h3><quotetitle>')
    text = text.replace('</quotetitle></h3></p>', '</quotetitle></h3>')
    text = text.replace('</quotetitle></h3><br>\r\n', '</quotetitle></h3>\r\n<p>')
    text = text.replace('\r\n<p></p>', '')
    return md, text


def finalize_markdown(text):
    def trans_quotetitle(match):
        return _("Posted by %(user)s") % {'user': match.group('content')}
    text = re.sub(r'<quotetitle>(?P<content>.+)</quotetitle>', trans_quotetitle, text)
    text = re.sub(r'<quotesingletitle>', _("Quote"), text)
    return text