# spvs-calc
SPVS (sexagesimal) calculator script.  Written for python3.  Currently supports multiply, add, subtract.

Usage:
<<<<<<< HEAD
- python3 ./calculator.py \<options\> \<command\>

Supported Options:
- \-c OR \--cull &emsp; Culls trailing zeroes (real SPVS style)


Supported Commands:
- add \<a\> \<b\> &emsp; Addition
- sub \<a\> \<b\> &emsp; Subtraction
- mult \<a\> \<b\> &emsp; Multiplication
- inv \<a\> \<digitDepth\> &emsp; Brute force inverse search to specified digit depth
=======
- python3 ./calculator.py \<command\>


Supported Commands:
- add \<a\> \<b\>
- sub \<a\> \<b\>
- mult \<a\> \<b\>
>>>>>>> 804c604707247435e88526c99c39762a8701a853


Infix is also supported with '+', '-' and 'x', i.e
- \<a\> \+ \<b\>
- \<a\> \- \<b\>
- \<a\> x \<b\>

Note that for infix multiplication, the letter 'x' must be used, as '\*' is a special character.  

Use argument 'h' or 'help' for extended usage options.
