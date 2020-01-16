/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/
class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node* dc;
        Node* head_iter = head;
        Node* dc_iter;
        unordered_map<Node*, Node*> dc_hash;    //key: head's pointer    value: dc's pointer
        
        if(head_iter != NULL){
            dc = new Node(head_iter->val);
            dc_iter = dc;
            dc_hash.insert(make_pair(head_iter, dc_iter));
        }else{
            return NULL;
        }
        
        //set value and next pointer
        while(head_iter->next != NULL){
            head_iter = head_iter->next;
            dc_iter->next = new Node(head_iter->val);
            dc_iter = dc_iter->next;
            
            dc_hash.insert(make_pair(head_iter, dc_iter));
        }
        

        head_iter = head;
        dc_iter = dc;
        //set random pointer
        while(dc_iter != NULL){
            if(head_iter->random == NULL){
                dc_iter->random = NULL;
            }else{
                dc_iter->random = dc_hash.find(head_iter->random)->second;
            }
            dc_iter = dc_iter->next;
            head_iter = head_iter->next;
            
        }
        
        return dc;
    }
};
