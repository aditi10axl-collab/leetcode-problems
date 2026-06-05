struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode extra;
    extra.next = head;
    
    struct ListNode *f = &extra;
    struct ListNode *s = &extra;
    
    for (int i = 0; i < n; i++) {
        f = f->next;
    }
    
    while (f->next != NULL) {
        f = f->next;
        s = s->next;
    }
    
    s->next = s->next->next;
    
    return extra.next;
}
