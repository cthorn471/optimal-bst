optimal-bst
===========

Find the optimal binary search tree based on probabilities of keys

##### Usage

optimal-bst.py [-h] [--p P [P ...]] [--q Q [Q ...]]

##### Examples

```
$ python optimal-bst.py --p .15 .1 .05 .1 .2 --q .05 .1 .05 .05 .05 .1

k[2] is the root
k[1] is the left child of k[2]
d[0] is the left child of k[1]
d[1] is the right child of k[1]
k[5] is the right child of k[2]
k[4] is the left child of k[5]
k[3] is the left child of k[4]
d[2] is the left child of k[3]
d[3] is the right child of k[3]
d[4] is the right child of k[4]
d[5] is the right child of k[5]
```
