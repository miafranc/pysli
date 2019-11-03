# pysli

## Introduction

**pysli** is a one-command markup language or micro-system for creating verbatim PDF slides, mostly (programming) tutorials.

The only command one can use is the new slide command, `+++`, i.e. three plus signs alone on a new line:

```
Slide one
---------

This is the text of the first slide.

+++

Slide two
---------

This is the text of the second slide. 

```

## Requirements

* python
* LaTeX (beamer, upquote, textcomp) - `upquote` and `textcomp` are needed in order to properly handle single quotes, 
i.e. representing them by a straight apostrophe to be able to copy from the generated PDF file and use it as it is


## Using pysli

```
usage: pysli.py [-h] -d outdir filename

Create verbatim PDF slides using the smallest (one-command) markup language.

positional arguments:
  filename    input filename

optional arguments:
  -h, --help  show this help message and exit
  -d outdir   output directory
```

## Notes

* The aspect ratio is set to `16:9`.
* The slides (frames) are vertically centered.
* Setting the font size to `10pt` and the left margin to `2em`, the optimal maximum length of a row is 80 characters. 
(However, a maximum of 83 characters fit in a row and remain visible.) 
* A maximum of 20 rows can be put on one slide.
