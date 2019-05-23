# Post-Encoding Instructions
This document describes how to add a novel to the dataset. Before a novel is submitted it must be encoded using the instructions found in the document [Prose Fiction Encoding Instructions](https://handbook.ge1789.org/encoding-instructions/).

## Ubuntu for Windows
Much of the work we do in this tutorial will be done on the command line (bash shell). If you have a Windows machine with Windows 10, you can get access to this by downloading Ubuntu for Windows from the [Microsoft Store]("https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab=pivot:regionofsystemrequirementstab").

## Getting Set Up
1. Create a folder on your desktop in which you can store encoded texts and your local Git repository.
1. Download completed text from GitHub. Save text with the correct filename.

## Standardizing  Dashes, Quotation Marks, and Apostrophes.
1. Open the Terminal window (in Windows you can type bash or Ubunutu in the search bar).
1. Change the working directory `cd` to the folder in which you placed the encoded text.
1. Paste the following script into the command line, replacing `<FILENAME>` with the actual filename:
```
FILENAME=<FILENAME> && \
    TMPFILE=$(mktemp) && \
    smartypants $FILENAME | \
    python3 -c'import html,sys;print(html.unescape(sys.stdin.read()), end="")' > $TMPFILE && \
    cp $TMPFILE $FILENAME
```
4. Place the quality_control_checks.py script from https://github.com/random-canon/random-canon/tree/master/scripts in the same folder with the encoded text.
5. On the command line enter `python3 quality_control_checks.py <FILENAME>` replacing `<FILENAME>` with the actual filename.
6. The script will produce a list of errors if there are any. If there are no errors, the command prompt will return.
7. Repeat step 5 to ensure the errors were corrected. There may be errors related to non-ascii characters that do not need to be corrected (if, for example, the text really does contain an accented character).

The text should now be ready to be submitted to the random-canon Github repository!

## Working with Git/GitHub for the first time
The steps in this section will probably only need to be done once the first time you work with git.

1. Open the terminal window.
1. To see if git is installed and what version type `git --version` into the command prompt.
1. Set up your username and email with git by typing the following two commands in the command prompt:
  - `git config --global user.name "YOUR_USERNAME"` (use your GitHub username in place of YOUR_USERNAME)
  - `git config --global user.email "your_email_address@example.com"` (use your GitHub email in place of your_email_address@example.com)
  - To check that the correct information has been configured enter the following command: `git config --global --list`.
1. Now that we have git set up. We are going to make a copy of the Random Canon repository in GitHub (remote) and copy that to our machine (local). Go to the [Random Canon repository on Github](https://github.com/random-canon/random-canon).
1. Click  on the button that says `Fork` at the top right. Now you have your own copy of the Random Canon repository on Github. Next we want clone this fork on to our local machine to work with.
1. In the Terminal window navigate to where you want to store this repository on your machine using the `cd` (change directory) command. For ease, you may want to store it in the same folder you created for the encoded texts and the quality control script.
1. Enter the following command:
 `git clone https://github.com/YOUR_USERNAME/random-canon.git` replacing YOUR_USERNAME with your GitHub username. (You can also get the URL for your repository if you go to your forked repository on GitHub, select the green "Clone or Download" button on the main page, and copy the URL.)

## Adding an Encoded Novel
Now that git is configured and we have a copy of the repository saved locally, we are ready to add the encoded novels to the repository!

1. To begin, open the Terminal and change the working directory to the clone of the Random Canon repository on your local machine.
1. 	Each time you want to add novels you should create a branch in your local copy of the repository. Each branch can hold multiple files and commits, but there should only be one pull request (PR) per branch. To create a new branch: ``git branch next-batch``. (You can name the branch anything you like--it does not need to be ``next-batch``.)
1.	Change to this branch with ``git checkout next-batch``.  (Note: You can always check which branch you are on with just `git branch`).
1.	Place the contributed file in the ``texts`` subdirectory, verifying that it has the correct filename. You can do this as you would normally move files in the Windows File Explorer.
1.	`cd texts` to change the working directory to the texts folder. Add the file to the working index with ``git add FILENAME``. You Replacing the actual filename with `FILENAME`. (TIP: After you type the first few characters of the filename, you can press `TAB` button on your keyboard to fill in the rest of the filename.)
1.	Next we want to commit the file.
  - If you are encoder you can use ``git commit`` to commit the files you just added.
  - If you are not the person who encoded the file, set the author to the encoder with
  `git commit --author="Firstname Lastname <email@example.org>"`
  - If you are working with files encoded by more than one person, you may want to `git add` and then `git commit` files by one encoder at a time.
    - You can also add a message that explains what is being committed by appending `-m "Message"` to the `git commit` like "Added texts 1234, and 5678". This whole command looks like
  ```
  git commit --author="Firstname Lastname <email@example.org>" -m "message text here"
  ```
    or `git commit -m "message text here"` if you are the encoder.
5.	Push the branch to your remote repository on GitHub with  ``git push origin branch-name``.)
6.	Create a pull request in the browser. Go to the [original repository](https://github.com/random-canon/random-canon) on GitHub. You should see a notification on the repository's main page saying that you just pushed a branch. Click the green button that says `Compare & Pull request`.
7. In the drop down menus set the base repository as random-canon/random-canon, the base as master, the head repository as YOUR_USERNAME/random-canon and the head as YOUR BRANCH (i.e., the branch you created for this pull request). Then select the green button that says `Create Pull Request`

## Synchronizing with the main repository

At some point, you may want to bring your fork up to date with the original repository. The steps to do so are as follows:

1. Open the Terminal window and change the working directory to your local copy of the repository.
1. To see your remote repository (i.e. the fork you created on GitHub) type: `git remote -v`. You should see something like this:
```
origin  https://github.com/YOUR_USERNAME/random-canon.git (fetch)
origin  https://github.com/YOUR_USERNAME/random-canon.git (push)
```
1. Now we want to add the original Random Canon repository as our upstream repository with
```
 git add remote upstream https://github.com/random-canon/random-canon.git
 ```

 (Note: You should only need to do this step once)
1. Now if you run `git remote -v`. You should see something like this:
```
origin  https://github.com/ayarnell/random-canon.git (fetch)
origin  https://github.com/ayarnell/random-canon.git (push)
upstream        https://github.com/random-canon/random-canon.git (fetch)
upstream        https://github.com/random-canon/random-canon.git (push)
```
1. `git fetch upstream`
1. `git checkout master`
1. `git merge upstream/master`
1. `git push origin master`
