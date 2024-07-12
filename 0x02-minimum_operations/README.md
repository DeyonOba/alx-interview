# 0x02 Minimum Operation

<html>
  <body>
    <h1>0x02 Minimum Operation</h1>
    <hr heigth="20px"/>
    <h2>Requirements</h2>
    <ul>
      <li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
      <li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using <code>python3</code> (version 3.4.3)</li>
      <li>All your files should end with a new line</li>
      <li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
      <li>Your code should be documented</li>
      <li>Your code should use the <code>PEP 8</code> style (version 1.7.x)</li>
      <li>All your files must be executable</li>
    </ul>    
  </body>
</html>

## Set UP
Create a Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```
Install dependency
```bash
pip install -r requirements.txt
```

## Tasks
### 0. Minimum Operations
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

- Prototype: `def minOperations(n)`
- Returns an integer
- If n is impossible to achieve, return 0
  Example:
  
  n = 9
  
  H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
```bash
user@host:~/0x02-minoperations$ cat 0-main.py
```
`file_name`: [0-main.py](https://github.com/DeyonOba/alx-interview/blob/main/0x02-minimum_operations/0-main.py)
```python
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```
Run and test code like this
```bash
user@host:~/0x02-minoperations$
user@host:~/0x02-minoperations$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
user@host:~/0x02-minoperations$ pep8 0-minoperations.py
```
**Check the `0-minoperations.py` file for code implementations**
<hr height="40px" />

***THANKS FOR READING*** 👍
***
