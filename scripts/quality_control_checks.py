"""Check quality of encoding of a text."""
import argparse
import re
import subprocess
import sys

import lxml.html

parser = argparse.ArgumentParser(description='Check quality of encoding of a text.')
parser.add_argument('filename', type=str)

NON_ASCII_FREQUENT = set(r"""´‘’“”—àâæçÇéÉèêîôœû""")


def _pass_or_fail(success):
    print('✓' if success else '✗')
    if not success:
        sys.exit(1)


def main(filename):
    with open(filename) as fh:
        html = fh.read()
    text = lxml.html.fromstring(html).text_content()

    print('checking whether <i> is used for italics', end='')
    _pass_or_fail('<em>' not in html)

    print('checking for en-dashes (em-dashes prescribed)', end='')
    _pass_or_fail('–' not in text)
    print('checking for horizontal bars (em-dashes prescribed) ', end='')
    _pass_or_fail('―' not in text)

    print('checking for straight quotation marks ', end='')
    _pass_or_fail('"' not in text.replace(r'<meta charset="utf-8">', ''))

    print('checking for straight apostrophes ', end='')
    _pass_or_fail("'" not in text)

    print('checking for unintended ligatures ', end='')
    _pass_or_fail(not re.search(r'ﬀ|ﬁ|ﬂ', text))

    unusual_non_ascii = set(re.findall(r'[^\x00-\x7F]', text)) - NON_ASCII_FREQUENT
    if unusual_non_ascii:
        print(f'warning: {len(unusual_non_ascii)} unusual non-ascii char(s) found: ', end='')
        print(','.join(f'`{ch}` (U+{ord(ch):04X})' for ch in unusual_non_ascii))

    command = ['tidy', '-e', filename]
    print('checking for HTML5 errors with `tidy` ', end='')
    process = subprocess.run(command, check=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)  # noqa
    errors = int(re.search(r'([0-9]+) error', process.stdout).group(1))
    print('✓' if not errors else '✗')
    if errors:
        print('HTML5 errors found (ignore warning about `body` tag):')
        for line in process.stdout.splitlines():
            if line.startswith('About HTML Tidy:'):
                break
            print(line)

if __name__ == '__main__':
    args = parser.parse_args()
    main(args.filename)
