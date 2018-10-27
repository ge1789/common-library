Random Canon and Reprint Canon
==============================

This repository contains chapters (randomly sampled) from novels. The novels themselves are randomly sampled from two populations:

-	Novels published in the British Isles for the first time between 1837 and 1901 (**Random Canon**).
-	Novels in the above population which were still available (i.e., in print) in 2017 from Penguin, Oxford, or Broadview (**Reprint Canon**).

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
