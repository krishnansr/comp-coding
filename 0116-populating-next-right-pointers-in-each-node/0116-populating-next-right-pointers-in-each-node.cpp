/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        Node *_node = root;
        Node *next_level, *prev_node;
        
        while(_node != NULL && _node->left != NULL){
            next_level = _node->left;
            prev_node = NULL;
            while(_node != NULL){
                _node->left->next = _node->right;
                if(prev_node != NULL){
                    prev_node->right->next = _node->left;
                }
                prev_node = _node;
                _node = _node->next;
            }
            _node = next_level;
        }
        
        
        return root;
    }
};