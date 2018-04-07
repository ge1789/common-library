"""Check quality of encoding of a text."""
import argparse
import re
import subprocess
import sys

import lxml.html

parser = argparse.ArgumentParser(description='Check quality of encoding of a text.')
parser.add_argument('filename', type=str)

NON_ASCII_FREQUENT = set(r"""´‘’“”—àâæçÇéÉèêîôœû""")
OCR_LIGATURE_ERRORS = set('ﬀﬁﬂ')

def _pass_or_fail(success, message):
    if not success:
        print(message, '✗')
        sys.exit(1)


def main(filename):
    with open(filename) as fh:
        html = fh.read()
    text = lxml.html.fromstring(html).text_content()
    _pass_or_fail('<em>' not in html, 'checking whether <i> is used for italics')
    _pass_or_fail('–' not in text, 'checking for en-dashes (em-dashes prescribed)')
    _pass_or_fail('―' not in text, 'checking for horizontal bars (em-dashes prescribed) ')
    _pass_or_fail('‐' not in text, 'checking for Unicode hyphen (ASCII hyphen-minus prescribed) ')
    _pass_or_fail('"' not in text.replace(r'<meta charset="utf-8">', ''), 'checking for straight quotation marks')
    _pass_or_fail("'" not in text, 'checking for straight apostrophes')
    _pass_or_fail(not re.search('|'.join(OCR_LIGATURE_ERRORS), text),
                  f'checking for unintended ligatures ({",".join(OCR_LIGATURE_ERRORS)})')

    unusual_non_ascii = set(re.findall(r'[^\x00-\x7F]', text)) - NON_ASCII_FREQUENT
    if unusual_non_ascii:
        print(f'warning: {len(unusual_non_ascii)} unusual non-ascii char(s) found: ', end='')
        print(','.join(f'`{ch}` (U+{ord(ch):04X})' for ch in unusual_non_ascii))

    command = ['tidy', '-e', filename]
    process = subprocess.run(command, check=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)  # noqa
    errors = int(re.search(r'([0-9]+) error', process.stdout).group(1))
    if errors:
        print('checking for HTML5 errors with `tidy`', '✗')
        print('HTML5 errors found (ignore warning about `body` tag):')
        for line in process.stdout.splitlines():
            if line.startswith('About HTML Tidy:'):
                break
            print(line)
        sys.exit(1)

if __name__ == '__main__':
    args = parser.parse_args()
    main(args.filename)
