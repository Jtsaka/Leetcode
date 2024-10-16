class Solution {
    public TreeNode invertTree(TreeNode root) {
        if(root.right == null && root.left == null){
            return root;
        }
        TreeNode temp = root.right;
        root.right = root.left;
        root.left = root.right;

        invertTree(root.right);
        invertTree(root.left);
        
        return root;
    }
}
