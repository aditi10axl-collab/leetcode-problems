class Solution {
    List<Integer> res = new ArrayList<>();
    
    public List<Integer> postorderTraversal(TreeNode root) {
        if (root == null) return res;
        
        postorderTraversal(root.left);  // Left
        postorderTraversal(root.right); // Right
        res.add(root.val);              // Root
        
        return res;
    }
}
