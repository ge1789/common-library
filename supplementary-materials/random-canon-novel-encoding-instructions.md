Random Canon Novel Encoding Instructions
========================================

Version 1.1

In order to capture paragraph boundaries, novels will be encoded in plain text with a dash of HTML5.

**Examples**

The following lines show two paragraphs from a Victorian novel properly encoded:

```
<p>"Who is there?" cried a gruff voice from within.</p>
<p>"It is I, McMurdo. You surely know my knock by this time."</p>
```

Here are two more paragraphs. The second paragraph contains words in italics:

```
<p>"I suppose Mr. Banquier lends them to her?"</p>
<p>Not much use, for he's the type before whom a veritable <i>drame du coeur</i> might be played without his seeing any of it.</p>
```

**Instructions**

Follow these rules when encoding the text of a chapter.

1. Find a scan of the British first edition. Second editions and American editions often have differences. For example, the British first edition of *The Admiral's Ward* has 50 chapters; the American edition has 51 chapters.
1. Use a (plain) text editor to enter the contents of the text. (On macOS [Sublime Text](https://www.sublimetext.com/) seems to work well.)
2. Enter em-dashes (—) as two hyphens (--).
3. Use straight quotes (") and straight apostrophes (').
4. Enter accented characters (ë), ligatures (æ), and any characters not in the normal Latin alphabet directly ([macOS instructions](https://support.apple.com/en-us/HT201586)).
5. Enter italics using the ``<i>`` tag (``<i>italicized text</i>``).
6. Initial caps should be converted into normal case. For example, a chapter starting with all caps "THE" should be converted to "The").
7. Footnotes using superscripts in the original should be entered as follows in a way that preserves the spirit of the original.

    The following shows an example of how the appearance of the footnote should be entered:

    ```
    <p>Up goes a swarm of our <i>Ciompi</i>.<sup><a href="#fn2">2</a><sup></p>
    ```

    And add at the bottom of the document

    ```
    <section>
    <p id="fn2"><sup>2</sup> The poorer artisans connected with the wool trade—wool-beaters, carders, washers, etcetera.</p>
    </section>
    ```
8. Use HTML comments as needed to indicate unusual features of the text. For example: ``<p></p> <!-- extra space between paragraphs in the original. -->``
9. Start each document with the following:
    ```
    <!doctype html>
    <title>Chapter N of TITLE by AUTHOR</title>
    <meta charset="utf-8">
    ```

That's all.

Pass 2: Standardize Dashes, Quotation Marks, and Apostrophes
============================================================

*For reference only.* These steps will be taken automatically.

A second (automated) pass is required to standardize dashes and quotation marks.


Done on the command line (bash shell) with:

```
FILENAME=data/4123__trollope_barchester_towers_chp49of53_seed4123.html && \
    TMPFILE=$(mktemp) && \
    smartypants $FILENAME | \
    python3 -c'import html,sys;print(html.unescape(sys.stdin.read()), end="")' > $TMPFILE && \
    cp $TMPFILE $FILENAME
```

The command above requires the Python tool smartypants.


Pass 3: Quality Control
=======================

*For reference only.* These steps will be taken automatically.

1. Verify no en-dashes exist. (Sometimes a text will mistakenly use en-dashes instead of em-dashes.)
2. Verify no straight quotation marks exist.
3. Verify no straight apostrophes exist.
4. Verify no unintended (OCR artifact) ligatures exist (e.g., ﬀ, ﬁ, ﬂ). The easiest way to do this is to show all non-ASCII characters in a file: ``grep --color='auto' -P -n '[^\x00-\x7F]' 2629__payn_halves_chp30of32_seed2629.html``
5. Check for HTML5 errors with tidy: ``tidy -e 2629__payn_halves_chp30of32_seed2629.html``. Ignore the error about implicit ``<body>``, we do not use this tag; fix all other errors.

Useful notes:

- In Python 3 you can get the unicode code point for a non-ASCII character with ``ord``, e.g., ``ord('’')`` returns 8217 which is the code for right single quotation mark (used for possessives).

Wishlist
========
- Create a whitelist of non-ASCII characters which appear frequently. This will help identify a family of OCR errors.
