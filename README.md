# freeCodeCamp-Arithmetic-Formatter

## Instructions:
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter

## Purpose
### Input:
```python
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

### Output:
```python
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
  ```

## Preview:
<img src="https://github.com/iVuDang/freeCodeCamp-Arithmetic-Formatter/blob/main/Arithmetic%20preview.png" width=100% height=100%>

## Technologies: 
* Python

## Outcome :white_check_mark: :
| Website | Link | 
| ------------- | ------------- | 
| Replit demo | https://replit.com/@iVuDang/FCCArithmetic-FormatterTestv3#main.py | 

<br/>

- - - -

## What I learned:
1. Can use a combination of  'if (not in [list])'
'in' keyword is used to check if a value is present in a sequence (list, range, string etc.)

2. Need to use double quotations  when single quotations are used within a string. 
            " This is an 'example'" 


3. rjust() method  right aligns a string, it can be used to determine a fixed width for strings in different rows. 

            Syntax
            string.rjust(length, character)

            length - length of the returned string
            character - optional character to fill the missing space to the left of the string). 

            e.g. 
            number = 32

            number.rjust(2)
            32

            number.rjust(4)
            32

4. rstrip() method removes any trailing characters (characters at the end a 
string), space is the default trailing character to remove.

            Syntax
            string.rstrip(characters)

            We need to rstrip() because our last iteration has the 4 spaces at the end. 


## Citations:
* https://www.w3schools.com/python/ref_string_rjust.asp
* https://www.w3schools.com/python/ref_string_rstrip.asp
* rjust method and rstrip method ideas inspired from ZeynebBechiri 

