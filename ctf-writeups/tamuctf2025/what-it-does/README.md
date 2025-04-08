# What It Does

- Author: `flocto`
- Type: `Reverse Engineering`
- Original: https://github.com/tamuctf/tamuctf-2025/tree/main/rev/whatitdoes

## Solution

This challenge is a trap. A trap I say! It preys upon the weak who don't know any better.

There's an included python file called `WDID.py`. I'll spare you the details, but this file is useless if you just want to solve the challenge. If you really want to know, it's just a decision tree that spits out certain answers depending on the user's input.

Keep in mind that this ctf has flags with the pattern "gigem{*}". There is a file included called `flag.wdz` which, if you look at it vaguely, you can see a pattern:

```
A
M:k
YJ:1
M:g
NJ:1
A
M:m
YJ:1
M:i
NJ:1
A
M:F
YJ:1
M:g
NJ:1
A
M:h
YJ:1
M:e
NJ:1
A
M:l
YJ:1
M:m
NJ:1
```

Don't see it? Lemme only show you the lines that start with "m":

```
M:k
M:g
M:m
M:i
M:F
M:g
M:h
M:e
M:l
M:m
```

Still don't see it? Alright, I'll remove every other line starting with the first:

```
M:g
M:i
M:g
M:e
M:m
```

Whoa, that's crazy. Every other line is the flag (decision tree, remember?). We can just write a simple program (or grep) to print the flag

```python
with open("flag.wdz") as f:
    lol = 0
    lines = f.readlines()

    for line in lines:
        if(not "M:" in line):
            continue
        lol += 1
        if(lol % 2 == 0):
            print(line.replace("M:","").replace("\n",""), end="")
```

And whoa the flag is `gigem{it_does_what_it_does}` crazy

This truly was one of the "what if I just printed stuff lol" moments of all time
