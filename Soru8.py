# Binary tree yüksekliğini hesaplayan bir algoritma yazınız. Yükseklik veya derinlik,
# kök düğümden (root node) yaprak düğüme (leaf node) giden en uzun yoldaki toplam düğüm(node) sayısıdır.
# (Program, en uzun yoldaki toplam düğüm sayısını dikkate almalıdır. Örneğin, boş bir ağacın
# yüksekliği 0'dır ve yalnızca bir düğümü olan ağacın yüksekliği 1'dir.)
# Oluşturduğunuz programda aşağıdaki ağacı oluşturup yazdığınız algoritmayı test edin.
# Programınız sonuç olarak bu ağacın maximum yüksekliğini 3 olarak vermelidir.
# (İpucu: Recursive çözüm kullanabilirsiniz.)


#              15
#           /      \
#          /        \
#         10        20
#        /  \       / \
#       /    \     /   \
#      8     12   16   25


from Tree import Tree


tree = Tree()
tree.add(15)
tree.add(10)
tree.add(20)
tree.add(8)
tree.add(12)
tree.add(16)
tree.add(25)


def calculate_height_of_tree(node):
    if node == None:
        return 0

    left = calculate_height_of_tree(node.left)
    right = calculate_height_of_tree(node.right)

    return 1 + max(left, right)


print(calculate_height_of_tree(tree.root))
