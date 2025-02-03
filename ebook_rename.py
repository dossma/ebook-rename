from PyPDF2 import PdfReader
import ebookatty
import os
# import shutil
import pathlib
from glob import glob

"""
Explanation:
 Scan directory for pdf and epub files, extract title and author from metadata and replace its filename with these.
 When metadata is present, the program proposes for each file its renaming which the user can confirm or not.
 In case of confirmation, the program sets the pattern >title by author.pdf< (or .epub)
 Example: >messyname.epub< is being renamed to >Robinson Crusoe by Daniel Dafoe.epub<
 In case it should not be renamed as proposed, the program asks to rename it manually which you can skip as well.
 Hereby, you can check for each file if and how you want it to be renamed.

 Warning 1: Test this tool first on a small directrory for you to understrand how it works.
 Warning 2: Use this tool only for directories which do NOT contain sub-directories. 
"""

folder = r"C:\path\to\your\ebook\folder"  # Note: no final slash!

def main(folder):
    file_list = collect(folder)
    untouchedlist = []
    for file_old in file_list:
        try:
            file_new = parse(file_old, folder)
            if file_new is not None:
                file_new = rename(file_new, folder)
                save(file_old, file_new, folder, untouchedlist)
            else:
                # print("Datei", file_old, "hat keine meta-Einträge; wird übersprungen")
                untouchedlist.append(file_old)
                continue
        except Exception as e:
            print ("Datei", file_old, "liefert Fehler\n", e, "\n")
            untouchedlist.append("Fehler: " + str(e) + "-" + file_old)

    terminate(untouchedlist)


def collect(folder):

    pdf_files = glob(folder + '/**/*.pdf', recursive=True)  
    epub_files = glob(folder + '/**/*.epub', recursive=True)  
    file_list = pdf_files + epub_files

    return file_list


def parse(file, file_folder):
    ext = pathlib.Path(file).suffix  # pdf oder epub oder...
    if ext == ".pdf":  # pdf
        reader = PdfReader(file)
        meta = reader.metadata
        title = meta.title
        author = meta.author
    elif ext == ".epub":  # pdf
        meta = ebookatty.metadata.epub.Epub(file)
        title = meta.metadata["title"]
        author = meta.metadata["author"]
    else:  # Kein pdf und kein epub
        return

    if isinstance(title, str) and isinstance(author, str):
        file = file_folder + "\\"  + title + " by " + author + ext
    elif isinstance(title, str):
        if title != "untitled":
            file = file_folder + "\\" + title + ext
        else:
            file = None
    else:
        # print ("Kein Meta", file)
        file = None

    return file


def rename(filename, file_folder):
    # Unerlaubte Dateizeichen ersetzen

    filename = filename.split("\\")[-1]

    filename = filename.replace("\n", " - ")  # "\n" ersetzen mit Bindestrich
    filename = filename.replace("\\", "-")  # "n" ersetzen mit Bindestrich
    filename = filename.replace("/", "-")  # "/" ersetzen mit Bindestrich
    filename = filename.replace("?", "-")  # "/" ersetzen mit Bindestrich
    filename = filename.replace("\"", "!")  # "/" ersetzen mit Bindestrich
    filename = filename.replace(r"*", " ! ")  # "/" ersetzen mit Bindestrich
    filename = filename.replace(r"<", " ! ")  # "/" ersetzen mit Bindestrich
    filename = filename.replace(r">", " ! ")  # "/" ersetzen mit Bindestrich
    filename = filename.replace(r":", " - ")  # "/" ersetzen mit Bindestrich
    filename = filename.replace(r"|", "-")  # "/" ersetzen mit Bindestrich

    filename = file_folder + "\\" + filename

    return filename


def save(file_old, file_new, file_folder, untouchedlist):
    file_old_stripped = file_old.split("\\")[-1]
    file_new_stripped = file_new.split("\\")[-1]
    question = input("\nRename\n" + '\033[1m' + file_old_stripped + '\033[0m' + "\nto\n" + '\033[1m' + file_new_stripped + '\033[0m' + "?" +
                     "\npress y for yes, n for no, q to quit\n")
    # print("\n")
    if question == "y":
        os.rename(file_old, file_new)
    elif question == "n":
        man_filename = input("Type new file name including extension (or press \"n\" for skipping the file)\n")
        if man_filename != "n":
            file_new = file_folder + "\\" + man_filename
            os.rename(file_old, file_new)
        else:
            untouchedlist.append(file_old)
            pass
    else:
        terminate(untouched=untouchedlist)
        quit()

def terminate(untouched):
    print("\nDONE!\n")
    if untouched:
        print ("Not renamed were:")
        for x in zip(untouched):
            print(x)


if __name__ == '__main__':
    main(folder=folder)
    # files = collect(folder_orig)
    # parse(...)
    # rename(files)
    # save(...)
    # terminate(...)
