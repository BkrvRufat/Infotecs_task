# Comparing build protocols
__________________________________________
This script compare two log files, which are got by building C++ projects with make/CMake.
Script takes 2 files as input: log, txt, cmake, etc. Then program compare this files and as a result print strings that differ.

To see project in github check my [Repository](https://github.com/BkrvRufat/Infotecs_task)
## Requirements
__________________________________________
- OS
  - Windows
  - Linux
- Python3.x


## Installation (using global python)
__________________________________________
- `cd /to/project/root/`
- `python3 -m pip install --upgrade pip`
- `python3 -m pip install -r requirements.txt`
## Launch
__________________________________________
After installation modules, we should run the script as below:
```
python main.py 'path1' 'path2' 
```
Instead of '*path1*' and '*path2*' write your path log files name, which you want to compare.

If log files don't have differences, program will be printed:
```
Files are different only by date and path
```
If they have differences, as a result you'll get strings which are differ.
For example, this two strings are different:
```diff
DIFF LINE:111
"[ 81%] building c object source_subfolder/cmakefiles/zlib.dir/inffast.c.o"
vs
"[ 75%] building c object source_subfolder/cmakefiles/zlib.dir/inffast.c.o"
```
## Author
__________________________________________
* **Bakirov Rufat** - *Initial work* - [BkrvRufat](https://github.com/BkrvRufat)