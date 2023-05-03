from No import No

class ListaNos:
    def __init__(self, lista):
        self.texto = lista
        self.raiz = None
    
    def insere(self, novo):
        """Insere o nó na lista, incrementando a frequência caso o caractere já exista na lista."""
        for item in self.raiz:
            if item.conteudo == novo.conteudo:
                item.freq += 1
                self.raiz.sort(key=lambda no: no.freq)
                return
        self.raiz.append(novo)
        self.raiz.sort(key=lambda no: no.freq)
        
    def criaLista(self):
        """Cria uma lista de nós a partir do texto."""
        self.raiz = []
        for letter in self.texto:
            self.insere(No(letter, 1, '', None, None))
    
    def criaArv(self):
        """Cria uma árvore de Huffman a partir da lista de nós."""
        self.criaLista()
        while len(self.raiz) > 1:
            novo = No("", self.raiz[0].freq + self.raiz[1].freq, '', self.raiz[0], self.raiz[1])
            self.raiz.pop(0)
            self.raiz.pop(0)
            self.raiz.append(novo)
            self.raiz.sort(key=lambda no: no.freq)
        self.raiz = self.raiz[0]
