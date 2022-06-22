var isSameTree = function(p, q) {
    if (p === null && q === null) {
        return true;
    }
    if (!p || !q) {
        return false;
    }
    if (p.val !== q.val) {
        return false;
    }
    return isSameTree(p.right, q.right) && isSameTree(q.left, q.left);
};