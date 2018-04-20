# 移除未排序链表中的重复节点


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_dump(root: Node):
    node = root
    cache = [root.val]

    while node.next:
        if node.next.val not in cache:
            cache.append(node.next.val)
        else:
            node.next = node.next.next

        node = node.next

    return root


if __name__ == '__main__':
    first = Node(1)
    head = first

    for i in range(10):
        n = Node(i)
        first.next = n
        first = first.next
