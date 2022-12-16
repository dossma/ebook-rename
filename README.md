# ebook-file-renaming
Renaming pdf and epub files according to their metadata entries

[![NPM Version][npm-image]][npm-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url]

The program scans a directory, including subdirectories, for pdf and epub files, extract title and author from metadata and replace its filename with that.
When metadata is present, the program proposes for each file its renaming which the user can confirm or not.
In case of confirmation, the program sets the pattern >title by author.pdf< (or .epub)
Example: >messyname.epub< is being renamed to >Robinson Crusoe by Daniel Dafoe.epub<
In case it should not be renamed as proposed, the program asks to rename it manually which you can skip as well.
So for each file, you are in control if and how it should be renamed.
<!-- ![example image](header.png) -->

<img src="https://github.com/dossma/ebook-file-renaming/blob/main/header.png" width=50% height=50%>

## Get started

1. Download the file
2. Open it in your Python IDE
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
