# LogCombiner
A tool to combine Minecraft Logs

# Using
Run the commands:
```bash
git clone https://github.com/CAG2Mark/LogCombiner
cd LogCombiner
```
Create the a text file called `mcpath.txt` in the `LogCombiner` folder, and paste in the link to your Minecraft **root** folder.

### Using the log combiner

You can run the following command to run the log combiner: (note: the final log file may end up gigabytes in size!)
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
cat keywords.txt | searcher.py >results.txt
```

macOS/Linux/UNIX:
```bash
searcher.py <keywords.txt >results.txt
```
