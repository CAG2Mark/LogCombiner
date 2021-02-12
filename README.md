# LogCombiner
A tool to combine and search Logs

# Using

### Prerequisites
* Python 3
* Git (alternatively you can download this repo as a zip and extract it and `cd` into it later)

Run the commands:
```bash
git clone https://github.com/CAG2Mark/LogCombiner
cd LogCombiner
```
Create the a text file called `mcpath.txt` in the `LogCombiner` folder, and paste in the link to your **root**, such that the log .gz files are in <root>/Logs.

### Using the log combiner

You can run the following command to run the log combiner: (note: the final log file may end up gigabytes in size!)

Windows:
```powershell
py combiner.py
```

macOS/Linux/Unix:
```bash
python3 combiner.py
```

## Using the log searcher

To use the searcher (it searches for a specific keyword), make a file called `keywords.txt`. It should be in the following format:
```
keyword1 // these are keywords you want to search for
keyword2
... // and so on
confirm // put this after your keywords
-1 // this is how many files (starting from the most recent) are to be searched through. Enter -1 to search all files.
```
For example, if I wanted to search for "You have won the game" or "You have lost the game" in the last 5 files, this would be your `keywords.txt` file:
```
You have won the game
You have lost the game
confirm
5
```
You can then run the following command to run the search:

Windows:
```powershell
cat keywords.txt | py searcher.py >results.txt
```

macOS/Linux/UNIX:
```bash
python3 searcher.py <keywords.txt >results.txt
```
