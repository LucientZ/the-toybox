# Moving Slowly

- Author: `moveslow`
- Original: https://github.com/tamuctf/tamuctf-2025/tree/main/web/moving-slowly

## Solution
```
Allow me to scribe a tragedy
Famous? Not so
Of something that happened not so long ago

'tis a story of wit
A story of shame
A story about how AI is kinda lame

'twas a webpage with an AI guard
It sung its song just like a town bard 

Sing and sing it did
To the internet amid
Every password entered, incorrect 
Every character with force

String after string I tried
Until I felt like I died
Listening to this AI quip
Until I read the source

There it was, plain as day
That vuln must be it
`required` removed, empty string approved
Thought I that it had whit

I then let out my breath
Out came a courageous sigh
Quoth the webpage, 'gigem{m4yb3_n0t_everything_needs_ai}'
```

### The vuln in question

Basically, this was supposed to be a timing attack with an AI, but the author forgot to check if `len(input_password) == len(correct_password)` and empty string was a valid solution lol

```py
def compare_password(input_password):
    for i, char in enumerate(input_password): # <--- Unintentional Vuln here
        if char != correct_password[i]:
            print(i)
            silly_message = generate_silly_message()
            return False, silly_message  
    return True, None 
```
