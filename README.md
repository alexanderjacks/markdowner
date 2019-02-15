# Markdowner 🔪🔠🐍
## [alexanderjacks](https://github.com/alexanderjacks)

## 🛵 Use
- ```cd markdowner/``` (Go to this directory in Terminal.)
- ```python3 markdowner.py```
- Creates files in ```./mds/```

## 🔬 Detailed Function
Takes provided CSV & makes each line into a Markdown file.
1. Uses built-in ```.readlines()``` method to inhale CSV as list
2. Cleans syntax character from data with ```.split(\r)``` method.
3. Runs a ```while``` loop: 
* Builds a list of fields per line  ```.append()```
* Prints 1st list's items-- 2nd list is junk syntax from earlier
* Loops back to print next line of py list items
4. Writes all generated markdown to a file ```stdout_put.md```

## 🚩 Development Milestones
 - ✅ indent and add correct characters before/after fields
 - ✅ create Markdown (.md) file per record (CSV line)
 - add user prompts to script
 - modify markdown filename instead of defaulting to 1st field value
 - further custom options will be noted useful as development continues

## 📝 MIT License.
### Alexander Jacks, 2019.
