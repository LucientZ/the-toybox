# Brainrot

- Author: `flocto`
- Type: `Reverse Engineering`
- Original: https://github.com/tamuctf/tamuctf-2025/tree/main/rev/brainrot

## Preamble

You're going to have to hear me out on this one: this challenge is actually fun.

There's this thing in programming called an "esoteric language" (esolang for short) and it's a fascinating concept. What if we made programming languages, but like for art instead? An example of an esolang is [LOLCODE](https://en.wikipedia.org/wiki/LOLCODE), which is a programming language that speaks in lolspeak (look it up). Hello world in that language is:

```
HAI 1.2
CAN HAS STDIO?
VISIBLE "HAI WORLD!"
KTHXBYE
```

[Dreamberd](https://github.com/TodePond/GulfOfMexico) (Now "Gulf of Mexico") is another esolang which looks like this:

```js
const const hello = "Hello World"!
if (;false) {
   print(hello)?
}
```

This prints "Hello World" along with displaying debug information on the print statement.

Some esolangs play off of other languages and make them borderline undreadable. Enter [pygyat](https://github.com/shamith09/pygyat), an esolang which uses language which would make our forefathers' minds explode. It replaces many python keywords with verbal atrocities. This is where our story begins for the challenge.

## Solution

This challenge has a program in pygyat. Don't worry if you can't read it, I'll fix it later. This is the code:

```py
###############
#  brain.gyat #
###############
lock in hashlib glaze sha256

skibidi Brain:
    bop __init__(unc, neurons):
        unc.neurons = neurons
        unc.thought_size = 10

    bop brainstem(unc):
        its giving sha256(",".join(str(x) mewing x diddy sum(unc.neurons, [])).encode()).hexdigest()

    bop rot(unc, data):
        mewing i diddy huzz(len(data)):
            unc.neurons[(3 * i rizz 7) % unc.thought_size][(9 * i rizz 3) % unc.thought_size] ^= data[i]

    bop think(unc, data):
        thought = [0] * unc.thought_size
        mewing i diddy huzz(unc.thought_size):
            thought[i] = sum(unc.neurons[i][j] * data[j] mewing j diddy huzz(unc.thought_size))
        unc.neurons[:-1] = unc.neurons[1:]
        unc.neurons[-1] = thought
        its giving thought

#############
#  rot.gyat #
#############
lock in brain glaze Brain

healthy_brain = [[71, 101, 18, 37, 41, 69, 80, 28, 23, 48], [35, 32, 44, 24, 27, 20, 34, 58, 24, 9], [73, 29, 37, 94, 27, 58, 104, 65, 116, 44], [26, 83, 77, 116, 9, 96, 111, 118, 52, 62], [100, 15, 119, 53, 59, 34, 38, 68, 104, 110], [51, 1, 54, 62, 56, 120, 4, 80, 60, 120], [125, 92, 95, 98, 97, 110, 93, 33, 128, 93], [70, 23, 123, 40, 75, 23, 104, 73, 52, 6], [14, 11, 99, 16, 124, 52, 14, 73, 47, 66], [128, 11, 49, 111, 64, 108, 14, 66, 128, 101]]
brainrot = b"gnilretskdi ,coffee ,ymotobol ,amenic etulosba ,oihO ni ylno ,oihO ,pac eht pots ,pac ,yadot yarp uoy did ,pu lio ,eohs ym elkcub 2 1 ,sucric latigid ,zzir tanec iaK ,tac frumS ,yzzilg ,ekahs melraH ,tanec iaK ,raebzaf ydderF ,gnixamnoog ,hoesac ,relzzir eht rof ttayg ruoy tuo gnikcits ,reppay ,gnippay ,pay ,gniggom ,gom,ttalcobmob ,gnillihc gnib ,deepswohsi ,tor niarb ,oitar + L ,ozob L ,L ,oitar ,ie ie iE ,suoived ,emem seimmug revas efil dna seceip s'eseeR ,io io io ,ytrap zzir koTkiT ,teggun ,su gnoma ,retsopmi ,yssus ,suS ,elgnid eladnuaQ ,gnos metsys ym ni atnaF ,kcil suoived ,syddid ta sthgin 5 ,hsinapS ro hsilgnE .gnos teksirb ,agnizab ,bruc eht etib ,orb lil ,dulb ,ni gnihcram og stnias eht nehw ho ,neerb fo seert ees I ,sinneD ekud ,biks no ,ennud yvvil ,knorg ybab ,rehtorb pu s'tahw ,gab eht ni seirf eht tuP ,edaf repat wol ,yddid ,yddirg ,ahpla ,gnixxamskool ,gninoog ,noog ,egde ,gnigde ,raeb evif ydderf ,ekahs ecamirg ,ynnacnu ,arua ,daeh daerd tnalahcnon ,ekard ,gnixat munaF ,xat munaf ,zzir idibikS ,yug llihc ,eiddab ,kooc reh/mih tel ,gnikooc ,kooc ,nissub ,oihO ,amgis eht tahw ,amgis ,idibikS no ,relzzir ,gnizzir ,zzir ,wem ,gniwem ,ttayg ,teliot idibikS ,idibikS"[::-1]

brain = Brain(healthy_brain)
brain.rot(brainrot)

flag = input("> ").encode()
chat is this real not len(flag) twin 40:
    yap("i'll be nice and tell you my thoughts have to be exactly 40 characters long")
    exit()

required_thoughts = [
    [59477, 41138, 59835, 73146, 77483, 59302, 102788, 67692, 62102, 85259],
    [40039, 59831, 72802, 77436, 57296, 101868, 69319, 59980, 84518, 73579466],
    [59783, 73251, 76964, 58066, 101937, 68220, 59723, 85312, 73537261, 7793081533],
    [71678, 77955, 59011, 102453, 66381, 60215, 86367, 74176247, 9263142620, 982652150581],
]

failed_to_think = Cooked
mewing i diddy huzz(0, len(flag), 10):
    thought = brain.think(flag[i:i rizz 10])
    chat is this real thought != required_thoughts[i//10]:
        failed_to_think = Aura

chat is this real failed_to_think or brain.brainstem() != "4fe4bdc54342d22189d129d291d4fa23da12f22a45bca01e75a1f0e57588bf16":
    yap("ermm... you might not be a s""igma...")
only in ohio:
    yap("holy s""kibidi you popped off... go submit the flag")
```

As you can see, this is awful. However, it's literally just python, so you can translate it back to python by doing some multicursor shenanigans:

```py
#############
#  brain.py #
#############
from hashlib import sha256

class Brain:
    def __init__(self, neurons):
        self.neurons = neurons
        self.thought_size = 10

    def brainstem(self):
        return sha256(",".join(str(x) for x in sum(self.neurons, [])).encode()).hexdigest()

    def rot(self, data):
        for i in range(len(data)):
            self.neurons[(3 * i + 7) % self.thought_size][(9 * i + 3) % self.thought_size] ^= data[i]

    def think(self, data):
        thought = [0] * self.thought_size
        for i in range(self.thought_size):
            thought[i] = sum(self.neurons[i][j] * data[j] for j in range(self.thought_size))
        self.neurons[:-1] = self.neurons[1:]
        self.neurons[-1] = thought
        return thought

###########
#  rot.py #
###########

from brain import Brain

healthy_brain = [[71, 101, 18, 37, 41, 69, 80, 28, 23, 48], [35, 32, 44, 24, 27, 20, 34, 58, 24, 9], [73, 29, 37, 94, 27, 58, 104, 65, 116, 44], [26, 83, 77, 116, 9, 96, 111, 118, 52, 62], [100, 15, 119, 53, 59, 34, 38, 68, 104, 110], [51, 1, 54, 62, 56, 120, 4, 80, 60, 120], [125, 92, 95, 98, 97, 110, 93, 33, 128, 93], [70, 23, 123, 40, 75, 23, 104, 73, 52, 6], [14, 11, 99, 16, 124, 52, 14, 73, 47, 66], [128, 11, 49, 111, 64, 108, 14, 66, 128, 101]]
brainrot = b"gnilretskdi ,coffee ,ymotobol ,amenic etulosba ,oihO ni ylno ,oihO ,pac eht pots ,pac ,yadot yarp uoy did ,pu lio ,eohs ym elkcub 2 1 ,sucric latigid ,zzir tanec iaK ,tac frumS ,yzzilg ,ekahs melraH ,tanec iaK ,raebzaf ydderF ,gnixamnoog ,hoesac ,relzzir eht rof ttayg ruoy tuo gnikcits ,reppay ,gnippay ,pay ,gniggom ,gom,ttalcobmob ,gnillihc gnib ,deepswohsi ,tor niarb ,oitar + L ,ozob L ,L ,oitar ,ie ie iE ,suoived ,emem seimmug revas efil dna seceip s'eseeR ,io io io ,ytrap zzir koTkiT ,teggun ,su gnoma ,retsopmi ,yssus ,suS ,elgnid eladnuaQ ,gnos metsys ym ni atnaF ,kcil suoived ,syddid ta sthgin 5 ,hsinapS ro hsilgnE .gnos teksirb ,agnizab ,bruc eht etib ,orb lil ,dulb ,ni gnihcram og stnias eht nehw ho ,neerb fo seert ees I ,sinneD ekud ,biks no ,ennud yvvil ,knorg ybab ,rehtorb pu s'tahw ,gab eht ni seirf eht tuP ,edaf repat wol ,yddid ,yddirg ,ahpla ,gnixxamskool ,gninoog ,noog ,egde ,gnigde ,raeb evif ydderf ,ekahs ecamirg ,ynnacnu ,arua ,daeh daerd tnalahcnon ,ekard ,gnixat munaF ,xat munaf ,zzir idibikS ,yug llihc ,eiddab ,kooc reh/mih tel ,gnikooc ,kooc ,nissub ,oihO ,amgis eht tahw ,amgis ,idibikS no ,relzzir ,gnizzir ,zzir ,wem ,gniwem ,ttayg ,teliot idibikS ,idibikS"[::-1]

brain = Brain(healthy_brain)
brain.rot(brainrot)

flag = input("> ").encode()
if not len(flag) == 40:
    print("i'll be nice and tell you my thoughts have to be exactly 40 characters long")
    exit()

required_thoughts = [
    [59477, 41138, 59835, 73146, 77483, 59302, 102788, 67692, 62102, 85259],
    [40039, 59831, 72802, 77436, 57296, 101868, 69319, 59980, 84518, 73579466],
    [59783, 73251, 76964, 58066, 101937, 68220, 59723, 85312, 73537261, 7793081533],
    [71678, 77955, 59011, 102453, 66381, 60215, 86367, 74176247, 9263142620, 982652150581],
]

failed_to_think = False
for i in range(0, len(flag), 10):
    thought = brain.think(flag[i:i + 10])
    if thought != required_thoughts[i//10]:
        failed_to_think = True

if failed_to_think or brain.brainstem() != "4fe4bdc54342d22189d129d291d4fa23da12f22a45bca01e75a1f0e57588bf16":
    print("ermm... you might not be a s""igma...")
else:
    print("holy s""kibidi you popped off... go submit the flag")

```

There we go, this is so much better. 

We can see that the program verifies if you got the write flag in two different ways. The first is by making a hash of some values after giving the solution to the brain with `brain.brainstem()`. We obviously can't use this because it's a hash and hashes are (mostly) irreversable in a reasonable amount of time.

There *is* an operation that seems reversable however. This involves the second way the program checks if your input is incorrect:

```py
required_thoughts = [
    [59477, 41138, 59835, 73146, 77483, 59302, 102788, 67692, 62102, 85259],
    [40039, 59831, 72802, 77436, 57296, 101868, 69319, 59980, 84518, 73579466],
    [59783, 73251, 76964, 58066, 101937, 68220, 59723, 85312, 73537261, 7793081533],
    [71678, 77955, 59011, 102453, 66381, 60215, 86367, 74176247, 9263142620, 982652150581],
]

failed_to_think = False
for i in range(0, len(flag), 10):
    thought = brain.think(flag[i:i + 10])
    if thought != required_thoughts[i//10]:
        failed_to_think = True
```

The `required_thoughts` list have 40 values and we know our flag has 40 characters as per a previous check. The check also splits our string into chunks of 10 characters, similar to how `required_thoughts` is split into chunks of 10. If we take a look at `brain.think`, we can see why this is the case:

```python
def think(self, data):
        thought = [0] * self.thought_size # Creates a list of size 10 always since self.though_size = 10
        for i in range(self.thought_size):
            thought[i] = sum(self.neurons[i][j] * data[j] for j in range(self.thought_size))
        self.neurons[:-1] = self.neurons[1:]
        self.neurons[-1] = thought
        return thought
```

If we do some debugging on this function, we can actively see what it does to each 10-character chunk:

```py
# Using "aaaaaaaaaa" as an example
[52671, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[52671, 36375, 0, 0, 0, 0, 0, 0, 0, 0]
[52671, 36375, 53156, 0, 0, 0, 0, 0, 0, 0]        
[52671, 36375, 53156, 64990, 0, 0, 0, 0, 0, 0]    
[52671, 36375, 53156, 64990, 70519, 0, 0, 0, 0, 0]
[52671, 36375, 53156, 64990, 70519, 52186, 0, 0, 0, 0]
[52671, 36375, 53156, 64990, 70519, 52186, 92344, 0, 0, 0]
[52671, 36375, 53156, 64990, 70519, 52186, 92344, 61595, 0, 0]
[52671, 36375, 53156, 64990, 70519, 52186, 92344, 61595, 55193, 0]
[52671, 36375, 53156, 64990, 70519, 52186, 92344, 61595, 55193, 77115]
```

So each "thought" is really just the character multiplied by some constant. Luckily, the original state of the neurons is given to us because `brain.rot()` works in the same way the flag was created. This means that `self.neurons[i][j]` is a known value for any i, j with `data[j]` being unknown. Hmm, interesting. We have 10 unknown values and 10 equations... What could that mean???

If you've taken an algebra class, you know the answer. ~~The Substitution Method!~~ We're doing this with linear algebra actually I don't have time for the substitution method. Our matrix would look something like this given the first set of neurons:

```
/  71 101  45  37  41  69  80  28  23  48 \ / x_0 \   /  59477 \
|  35  32  44  24  27  88  34  58  24   9 | | x_1 |   |  41138 |
|  73  29  37  94  27  58 104  65  17  44 | | x_2 |   |  59835 | 
|  26   3  77 116   9  96 111 118  52  62 | | x_3 |   |  73146 |
| 100  15 119  53  86  34  38  68 104 110 | | x_4 | = |  77483 | 
|  51   1  54  62  56 120   4  10  60 120 | | x_5 |   |  59302 |
| 113  92  95  98  97 110  93  33 128  93 | | x_6 |   | 102788 |
|  70  23 123  86  75  23 104  73  52   6 | | x_7 |   |  67692 |
|  14  11  99  16 124  52  67  73  47  66 | | x_8 |   |  62102 |
\ 128  11  49 111  64 108  14  66 128 116 / \ x_9 /   \  85259 /
```

So obviously, we can simply ~~create a reduced row echelon form of the matrix and~~ make numpy solve our system of linear equations for us! We'll add a function to our `brain` to get the different values in the left and right matrices and just let numpy do the rest:

```py
    # Added to Brain class
    def get_coeffs(self, data):
        coeffs = []
        for i in range(self.thought_size):
            coeff_list = []
            for j in range(self.thought_size):
                coeff_list.append(self.neurons[i][j])
            coeffs.append(coeff_list)
        self.neurons[:-1] = self.neurons[1:]
        self.neurons[-1] = data
        return coeffs

# Used after a brain is made
for thought in required_thoughts:
    coeffs = numpy.array(brain.get_coeffs(thought))
    result = numpy.array(thought)
    solution = numpy.linalg.solve(coeffs, result)
    for result in solution:
        print(chr(round(result)), end="")
```

In the end, the program will spit out the flag:

```
gigem{whats_up_my_fellow_skibidi_sigmas}
```
