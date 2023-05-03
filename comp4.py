class No:
    def __init__(self, conteudo, freq, left, right):
        self.conteudo = conteudo
        self.freq = freq
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.conteudo} ({self.freq})"

    def is_leaf(self):
        return self.left is None and self.right is None
