__author__ = 'Tom'

class OptimalBST:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Find the optimal binary search tree from the probabilities of keys')
    parser.add_argument('--p', metavar='P', type=float, nargs='+', help='A list of probabilities for each key')
    parser.add_argument('--q', metavar='Q', type=float, nargs='+', help='A list of probabilities for each dummy key')
    args = parser.parse_args()
    bst = OptimalBST(args.p, args.q)

