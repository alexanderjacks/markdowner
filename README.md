# Markdowner 🔪🔠🐍
## [alexanderjacks](https://github.com/alexanderjacks)

## 🛵 Use
- ```cd markdowner/``` (Go to this directory in Terminal.)
- ```mkdir mds/```
- ```python3 markdowner.py```
- Creates files in ```./mds/```

## 🔬 Detailed Function
Takes provided CSV & makes each line into a Markdown file.
1. Uses built-in ```.readlines()``` method to inhale CSV as list
2. Cleans syntax character from data with ```.split(\r)``` method.
3. Runs a ```while``` loop: 
* Builds a list of fields per line  ```.append()```
* Prints 1st list's items-- 2nd list is junk syntax from earlier
* Writes generated markdown to file ```title.md``` per line, based on 1st key:value
* Loops back to print/write next line of py list items

## 🚩 Development Milestones
 - ✅ indent and add correct characters before/after fields
 - ✅ create Markdown (.md) file per record (CSV line)
 - add user prompts to script
 - modify markdown filename instead of defaulting to 1st field value
 - further custom options will be considered as development continues

## 📝 MIT License.
### Alexander Jacks, 2019.
