def levelOrder(self, root):
    ret = []

    level = [root]

    while root and level:
        currentNodes = []
        nextLevel = []
        for node in level:
            currentNodes.append(node.val)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        ret.append(currentNodes)
        level = nextLevel


    return ret
