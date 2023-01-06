/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func middleNode(head *ListNode) *ListNode {
    nodes := []ListNode{*head}
    for head.Next != nil {
        nodes = append(nodes, *head.Next)
        head = head.Next
    }
    idx := (len(nodes)-1)/2
    idx += (len(nodes)-1)%2
    midNode := nodes[idx]
    return &midNode
}