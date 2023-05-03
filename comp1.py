from ListaNos import ListaNos
from HuffmanTree import HuffmanTree

def read_file(file_name):
    """Reads the initial text from a file."""
    try:
        with open(file_name, "r") as file:
            text = file.read()
    except IOError:
        print("Erro ao abrir o arquivo")
    return text

def write_file(file_name, binary_data):
    """Writes binary data to a file."""
    try:
        with open(file_name, "wb") as file:
            file.write(binary_data)
    except IOError:
        print("Erro ao criar o arquivo")

# Main function
if __name__ == "__main__":
    # Read input text from a file
    input_text = read_file("abra.txt")
    input_chars = list(input_text)

    # Create a Huffman tree and a list of nodes
    huffman_tree = HuffmanTree()
    node_list = ListaNos(input_chars)
    node_list.create_tree()
    huffman_tree.encode(node_list.root)

    # Write the result to a file
    result_binary = huffman_tree.tree_to_binary(node_list.root) + huffman_tree.encode_text(node_list.root, input_text)
    write_file("result.txt", result_binary)

    # Print the result
    print("Arvore pre-ordem: " + huffman_tree.tree_to_binary(node_list.root))
    print(huffman_tree.encode_text(node_list.root, input_text))
    print(huffman_tree.decode_text(node_list.root, huffman_tree.encode_text(node_list.root, input_text)))
