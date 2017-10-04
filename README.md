# Challenge 3 - Bit counting

So when I saw this it reminded me of something I did recently where I would find the difference between two strings using the Levenshtein distance algorithm. I looked back at that and found that the difference in substitutions only is the Hamming distance, and the population of the on-bits in a bit string is known as the * Hamming Weight *. Thanks for this challenge, I hadn't heard of hamming weight before.

Anyway, before I'd looked at the Hamming weight stuff I had figured that I'd try and switch off bits until I got to 0. I noticed on the wiki page that there was an algorithm that could be faster than this but I had to know the architecture beforehand. You mentioned in the brief that I could assume a 64-bit int, but the only way to ensure that would be importing numpy (afaik, python doesn't have a `int_64` type and allows `int` only). While importing a well used module like numpy is not a problem in itself, the loop solution seems more portable. I like portable. 

## Usage

```
python counter.py [int_to_count]
```