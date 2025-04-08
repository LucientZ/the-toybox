# OTP

- Author: `nhwn`
- Type: `Reverse Engineering`
- Original: https://github.com/tamuctf/tamuctf-2025/tree/main/rev/otp

## Solution

Me when I `xor` Me when I `xor` Me when I xor the flag and `xor` and `xor` and `xor` Me when I xor the flag and `xor` Me when I xor the flag and then I re-xor some known value to get it back?????

This challenge works off of a principle that has been known for years, yet for some reason it blows people's minds when it's said. xor isn't encryption. Let's look at what xor does:

|a  |b  | Result |
|:--|:--|-------:|
|0  |0  |       0|
|1  |0  |       1|
|0  |1  |       1|
|1  |1  |       0|

"One or the other, but not both" as the saying goes. This is a good way of thinking about it, but another way is that "1 cancels out 1 in an xor". Why is this useful? Because we can chain the `xor` operation to go backwards! Let's say we have a key of `1` and any arbitrary 1-bit message. The only two possible solutions are:


|msg|key|*Result*|
|:--|:--|-------:|
|0  |1  |       1|
|1  |1  |       0|

Now, look what happens when we xor the result with the key *or* the message

|Result|key|*msg*|
|:--   |:--|----:|
|0     |1  |    1|
|1     |1  |    0|

|Result|msg|*key*|
|:--   |:--|----:|
|0     |1  |    1|
|1     |0  |    1|

We can extract either the key with the message or the message with the key. Meaning either if you xor a result with its key, you get back the message. This means if you have either, you win.

This binary has a coredump, meaning we can see what memory the program had at the moment of the dump. If we take a look at the otp function which obfuscates the original message, we can see clearly that it coredumps on the final call to the function:

```c
void otp(unsigned char* p, int n, int depth) {
    char key[128];

    read(RANDOM_FD, key, n);
    for (int i = 0; i < n; ++i) {
        p[i] ^= key[i];
    }

    if (depth < KEYS - 1) {
        otp(p, n, depth + 1);
    } else {
        dump();
    }
}
```

This is awesome because the function is recursive, meaning every `key[128]` array is currently on the stack because *every* call to `otp()` creates a new stack frame with a new `key[128]`. If we use gdb, we can just `bt full` with the coredump loaded to get what each key is.

```py
#4  0x00000000004012b2 in otp (p=0x7ffe603d01d0 "\203U\263k\221\221\031\017\206\bz\350$q\240v\352wN\037\236\253\371\024\200\335LT\264/\232\001!S\271r\221\r1\303\020\277\246Kr(\225'p1\333N\005\334\353\327r\357\177\n\376\177", n=0x3b, depth=0x3e7) at /otp.c:29
        key = "8\t\210\2673\351\\\0344\001\267\212\377{a\264Ǿ^\367\234<\327wD\364\000D\003\024\361`\364\205/\005]j\370}\207\353$\035\b|\240\250G\371\330 \031\213~Z\b\365-\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\211\036@\000\000\000\000"
#5  0x00000000004012a6 in otp (p=0x7ffe603d01d0 "\203U\263k\221\221\031\017\206\bz\350$q\240v\352wN\037\236\253\371\024\200\335LT\264/\232\001!S\271r\221\r1\303\020\277\246Kr(\225'p1\333N\005\334\353\327r\357\177\n\376\177", n=0x3b, depth=0x3e6) at /otp.c:27
        key = "\026\033\274Tv\264\350\351I{-\247@\303O\201\234jE\350f\224\006a\302\307\317交V\270Ϯ %\252Te\207\306\031\3560\353\214Uףh\245\312 \177\026R\3727\334\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\211\036@\000\000\000\000"
#6  0x00000000004012a6 in otp (p=0x7ffe603d01d0 "\203U\263k\221\221\031\017\206\bz\350$q\240v\352wN\037\236\253\371\024\200\335LT\264/\232\001!S\271r\221\r1\303\020\277\246Kr(\225'p1\333N\005\334\353\327r\357\177\n\376\177", n=0x3b, depth=0x3e5) at /otp.c:27
        key = "<\021\206\341}\320\325ɻ\335D4\253\220F\274\347\350\374/\341,m\324q\310P\236\304{\316\312}(\343\034\231\377\307\023q\231\217\247\331cQ\245\016\362\313l\301\301\223A;s&\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\211\036@\000\000\000\000"

#You get the idea...
```

I might be a terrible programmer, but for some reason I could *not* get this to work in python, so I did the next best thing and used c++. This was especially nice because characters are actually bytes and not goofy string objects (I know it isn't *technically* in the standard that they're a byte).

The whole solution is in the `/src/` directory, but it really boils down to applying `xor` of every key and then winning. It's not the most memory-safe solution, but it was the easiest. 

The program finally spits out the following:

```
gigem{if_you_did_that_manually_i_am_so_sorry_for_your_loss}
```

FIN