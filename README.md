# Markdowner 🔪🔠🐍
![https://github.com/alexanderjacks](## alexanderjacks)

## 🛵 Use
- ```cd markdowner/``` (Go to this directory in Terminal.)
- ```python3 markdowner.py```
- Note: does not yet generate markdown files, but prints to Terminal

## 🔬 Detailed Function
Takes provided CSV & makes each line into a Markdown file.
+ Uses built-in ```.readlines()``` method to inhale CSV as list
+ Cleans syntax character from data with ```.split(\r)``` method.
+ Runs a ```while``` loop: 
..* Builds a list of fields per line  ```.append()```
..* Prints 1st item of each line list-- 2nd is junk syntax from earlier

## 🚩 Development Milestones
+ create Markdown (.md) file per record (CSV line)
+ indent and add correct characters before/after fields

+ add user prompts to script
..* modify markdown filename instead of defaulting to 1st field value
..* further custom options will be noted useful as development continues

## Alexander Jacks, 2019.
### 📝 MIT License.
