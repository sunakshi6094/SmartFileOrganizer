\# Smart File Organizer



A Python command-line tool that automatically organizes files into folders based on their file type.



\## Features



\- Organizes files by extension

\- Supports documents, PDFs, images, videos, audio files, and archives

\- Places unknown file types into an `Others` folder

\- Prevents accidental file overwriting

\- Automatically renames duplicate files

\- Provides clear error messages

\- Handles invalid folder paths safely

\- Handles Ctrl+C interruption safely

\- Uses proper exit codes

\- Includes automated unit tests

\- Provides built-in `--help` documentation



\## Requirements



\- Python 3.10 or newer

\- No external Python packages are required



\## How to Run



```bash

python organizer.py "path/to/folder"





Example:



python organizer.py test\_files

Help

python organizer.py --help

Testing



Run the automated tests:



python -m unittest discover -s tests -v

Project Structure

SmartFileOrganizer/

├── organizer.py

├── tests/

│   └── test\_organizer.py

├── README.md

├── requirements.txt

├── .gitignore

└── venv/

Error Handling



The tool safely handles:



Missing folders

Invalid folder paths

File instead of folder

Duplicate filenames

File operation errors

Ctrl+C interruption



The program avoids showing raw Python tracebacks for expected errors.



Duplicate File Handling



The organizer never overwrites an existing file.



For example:



report.pdf

report\_1.pdf

report\_2.pdf

Example



Before:



test\_files/

├── document.pdf

├── photo.jpg

└── sample.txt



After:



test\_files/

├── PDFs/

│   └── document.pdf

├── Images/

│   └── photo.jpg

└── Documents/

&#x20;   └── sample.txt

Project Purpose



This project was developed as part of a Python Development Internship to demonstrate practical command-line development, input validation, error handling, safe file operations, and automated testing.







