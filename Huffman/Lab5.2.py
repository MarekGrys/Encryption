class Symbol:
    def __init__(self, symbol, waga):
        self.symbol = symbol
        self.waga = waga

    def __repr__(self) -> str:
        return f"{self.symbol}:{self.waga}"


class Node:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    @property
    def waga(self):
        return self.left.waga + self.right.waga

    def __repr__(self) -> str:
        return f"{self.left}-{self.right}"

    def getcode(self):
        res = dict()
        if isinstance(self.right, Node):
            for k, v in self.right.getcode().items():
                res["1" + k] = v
        else:
            res["1"] = self.right.symbol
        if isinstance(self.left, Node):
            for k, v in self.left.getcode().items():
                res["0" + k] = v
        else:
            res["0"] = self.left.symbol
        return res


def huffman(pkt, pwo):
    nodes = [Symbol(pkt[i], pwo[i]) for i in range(len(pkt))]
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.waga)
        a, b = nodes.pop(1), nodes.pop(0)
        nodes.append(Node(a, b))
    return dict((v, k) for k, v in nodes[0].getcode().items())


S = ["a", "b", "c", "d", "e", "f"]
P = [0.3, 0.1, 0.2, 0.1, 0.2, 0.1]
print(huffman(S, P))
S = ["a", "i", "s", "d"]
P = [0.2, 0.35, 0.25, 0.2]
print(huffman(S, P))
