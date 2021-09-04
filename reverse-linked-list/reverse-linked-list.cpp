/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

// class Solution {
// public:
//     ListNode* reverseList(ListNode* head) {
        
//         if(!head || !head->next) return head;
        
//         ListNode* prev = NULL;
        
//         while(head){
//             ListNode* next = head->next;
//             head->next = prev;
//             prev = head;
//             head = next;
//         }
        
//         return prev;
//     }
// };


class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        
        if(!head || !head->next) return head;
        
        ListNode* rest_head = reverseList(head->next); // rest_head - head of reversed ll (always be last node)
        
        ListNode* rest_tail = head -> next; // rest_tail - tail of reversed ll (head of original ll at last / curr node )
        
        head -> next = NULL; // setting next of last node of reversed ll as NULL
        
        rest_tail -> next = head; 
        
        return rest_head;
        
    }
};