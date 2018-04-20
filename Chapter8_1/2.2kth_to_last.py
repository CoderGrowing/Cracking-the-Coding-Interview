# 输入一个链表，输出该链表中倒数第k个结点。


def find_kth_to_tail(head, k):
    if not head:
        return
    before = head

    for i in range(0, k-1):
        before = before.next

    while before:
        before = before.next
        head = head.next

    print(head.val)
