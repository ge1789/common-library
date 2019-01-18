Random Canon and Reprint Canon
==============================

This repository contains chapters (randomly sampled) from novels. The novels themselves are randomly sampled (without replacement) from two populations:

-	Novels published in the British Isles for the first time between 1837 and 1901 (**Random Canon**). The sampling frame is restricted to novels for which there exist page images of the first edition as of 2018-12-31 11:59:59 UTC. Internet Archive, Google Books/HathiTrust, and the British Library are the only sources which are checked for page images.
-	Novels published in the British Isles for the first time between 1837 and 1901 which are still available ("in print") in 2017 from Penguin, Oxford, or Broadview (**Reprint Canon**).

Encoding instructions
---------------------

The encoding procedure used is described in [`novel-encoding-instructions.md`](novel-encoding-instructions.md).

Manifest
--------

-	`random_canon.csv` and `reprint_canon.csv` contain metadata about the chapters.
-	`scripts/quality_control_checks.py` checks to see if a text has been properly encoded.
-	`supplementary-materials` contains data used to construct the random samples.
-	`texts` contains chapters. Filenames begin with ATCL title ids. Texts are encoded using HTML5.
-	[`novel-encoding-instructions.md`](novel-encoding-instructions.md) describes the encoding process.
-	[`adding-an-encoded-novel.md`](adding-an-encoded-novel.md) describes how to add a novel to this repository.


Public Domain
-------------

All texts in this repository are in the public domain.
