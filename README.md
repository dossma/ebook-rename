# ebook-rename
This program renames your files by picking title and author from its metadata. 

_Example:_ `dafoe.epub` is being renamed to `Robinson Crusoe by Daniel Dafoe.epub`

## Motivation 
While people have a growing digital library, oftentimes the file names are messy and inconsistent. 

This program cleans up your files and you get a homogenous file name structure.

## Procedure
The program scans a directory for pdf and epub files.
For each file, when metadata is present, the program proposes its renaming which the user can confirm or not.
The proposed file name has the pattern `title by author.pdf` (or `....epub`).
In case you deny the proposed renaiming (for example when metadata is empty and the proposed file name is bad), the program asks you to rename it manually.
You then enter a new file name manually __or__ decide to leave its present file name.
So for each file, you are in control if and how it should be renamed.

<!-- ![example image](header.png) -->

<img src="https://github.com/dossma/ebook-file-renaming/blob/main/header.png" width=50% height=50%>

## Get started

1. Download the file
2. Open it in your Python IDE (Recommendation: [PyCharm](https://www.jetbrains.com/pycharm/))
3. Paste the target path into the variable quotes of `folder = r"C:\path\to\your\ebook\folder"`
4. Run  

Setting up a test folder for a first try is recommended as the file names will be overwritten.

## Development setup

Required external libraries are
- PyPDF2: https://github.com/py-pdf/PyPDF2
- ebookatty: https://github.com/alexpdev/ebookatty

```sh
pip install PyPDF2
pip install ebookatty
```

## Meta

Author: Jonas Dossmann

Distributed under the GPL-3.0 license.

[https://github.com/dossma/](https://github.com/dossma/)

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dossma/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dossma/node-datadog-metrics
[wiki]: https://github.com/dossma/ebook-file-renaming/wiki
