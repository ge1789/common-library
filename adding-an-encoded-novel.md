Adding an Encoded Novel
=======================

Version 0.2

This document describes how to add a novel to the dataset. Before a novel is
submitted it must be encoded using the instructions found in the document
["Random Canon Novel Encoding Instructions"](novel-encoding-instructions.md).

Steps
=====

*Note: work in progress*

These steps are taken after the final version of the chapter has been prepared. That is, they are taken after the conversion script and quality control script have been run.

1.	Create a branch in your fork of the repository. For example ``git branch next-batch``. Change to this branch with ``git checkout next-batch``. (You can name the branch anything you like--it does not need to be ``next-batch``.)
2.	Place the contributed file in the ``texts`` subdirectory, verifying that it has the correct filename.
3.	Add the file to the working index with ``git add``.
4.	Commit the file using ``git commit``. If you are not the person who encoded the file, set the author to the encoder with ``git commit --author="Firstname Lastname <email@example.org>"``.
5.	Push the branch to the remote with ``git push``. (You may need to issue the full version of the command, ``git push origin next-batch``.)
6.	Create a pull request in the browser.

Synchronizing with the main repository
======================================

*Note: work in progress*

You can switch back to the ``master`` branch with ``git checkout master`` at any time. ``git pull`` should synchronize your fork's master branch with your local branch.
