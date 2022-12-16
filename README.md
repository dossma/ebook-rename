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

Download the file, open in your Python IDE, paste the target path where your files are under the variable "folder" and run.  
Setting up a test folder for a first try is recommended as the file names will be overwritten.

## Development setup

Required libraries are
- PyPDF2: https://github.com/py-pdf/PyPDF2
- ebookatty: https://github.com/alexpdev/ebookatty
- os
- pathlib

```sh
pip install PyPDF2
pip install ebookatty
```

## Meta

Author: Jonas Dossmann

Distributed under the GPL-3.0 license. See ``LICENSE`` for more information.

[https://github.com/yourname/github-link](https://github.com/dossma/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
