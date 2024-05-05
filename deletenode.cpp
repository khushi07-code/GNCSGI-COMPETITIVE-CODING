/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
// if only node to be deleted given
class Solution {
public:
    void deleteNode(ListNode* node) {
        ListNode* temp=node;
        ListNode* rev=NULL;
        while(temp->next!=NULL)
        {
            temp->val=temp->next->val;
            rev=temp;
            temp=temp->next;
        }
        rev->next=NULL;
        
    }
};
