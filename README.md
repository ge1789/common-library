Random Canon and Reprint Canon
==============================

This repository contains chapters (randomly sampled) from novels. The novels themselves are randomly sampled (without replacement) from two populations:

-	Novels published in the British Isles for the first time between 1837 and 1901 (**Random Canon**). The sampling frame is restricted to novels for which there exist page images of the first edition as of 2018-12-31 11:59:59 UTC. Internet Archive, Google Books/HathiTrust, and the British Library are the only sources which are checked for page images. If the novel is a multivolume novel all volumes of the first edition must be available.
-	Novels published in the British Isles for the first time between 1837 and 1901 which are still available ("in print") in 2017 from Penguin, Oxford, or Broadview (**Reprint Canon**).

Encoding instructions
---------------------

The encoding procedure used is described in [Prose Fiction Encoding Instructions](https://handbook.ge1789.org/encoding-instructions/).

Manifest
--------

-	`random_canon.csv` contains metadata about the Random Canon titles.
-	`reprint_canon.csv` contains metadata about the Reprint Canon titles.
-	`other_novels.csv` contains metadata about texts included in the repository incidentally. These are not part of either Canon. These novels survive but there are no page scans of the first edition as of the end of 2018.
-	`scripts/quality_control_checks.py` checks to see if a text has been properly encoded.
-	`supplementary-materials` contains data used to construct the random samples.
-	`texts` contains chapters. Filenames begin with ATCL title ids. Texts are encoded using HTML5.
-	[`adding-an-encoded-novel.md`](adding-an-encoded-novel.md) describes how to add a novel to this repository.

Known issues
------------

- Curly quotation marks (``‘…’`` and ``“…”``) are not always entered correctly. Analyses should not require distinguishing between, say, ``“`` and ``”``. Counts of puncutation marks per sentence or paragraph, however, should be reliable.

Public Domain
-------------

All texts in this repository are in the public domain.

Contributors
------------

(in order of joining)

- Troy Bassett, Allen Riddell
- Laura Schneider
- Amy Yarnell
- Hannah Mills
- Rachel Condon
- Sarah Duke
