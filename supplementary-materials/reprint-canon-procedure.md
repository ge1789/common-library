Reprint Canon titles were selected by Troy Bassett via an SQL query.

The first query yielded the list in `Reprint Canon 3xSamples-version-1.xlsx`.
Sampling from this stopped when an error was encountered ("Gowers of Glenarne",
a title_id had been swapped). Bassett generated a second sample `Reprint Canon
3xSamples-version-2.xlsx` and AR continued collecting texts from that.

So the first five items in ``reprint_canon.csv`` are from `Reprint Canon 3xSamples-version-1.xlsx`:

1. Moths
2. What Maisie Knew
3. Cometh Up as a Flower
4. Jezebel's Daughter
5. The Master of Ballantrae

The remainder are from `Reprint Canon 3xSamples-version-1.xlsx`.

-----

For each book a chapter is chosen at random using the ATCL title ID as a random seed. (This is done so that others can verify that the chapters were sampled uniformly at random.)

Here's the bash command used to sample a chapter from Hardy's *The Hand of Ethelberta*:

```bash
TITLE_ID=5740 && TITLE_NAME=hardy_ethelberta && CHAPTERS=47 && \
  CHAPTER=$(python3 -c "import random;random.seed($TITLE_ID);print(random.randrange($CHAPTERS) + 1)") && \
  FILENAME="${TITLE_ID}__${TITLE_NAME}_chp${CHAPTER}of${CHAPTERS}_seed${TITLE_ID}.html" && \
  echo $FILENAME
```

which yields: ``5740__hardy_ethelberta_chp3of47_seed5740.html``.
