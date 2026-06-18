class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        output = 0
        connectedN = {}
        visited = set()

        for startN, endN in edges:
            if startN in connectedN:
                connectedN[startN].append(endN)
            else:
                connectedN[startN] = [endN]
            
            if endN in connectedN:
                connectedN[endN].append(startN)
            else:
                connectedN[endN] = [startN]

        def bfs(node):
            queue = [node]

            while queue:
                curr = queue.pop()
                if curr in connectedN:
                    for nextN in connectedN[curr]:
                        if nextN not in visited:
                            visited.add(nextN)
                            queue.append(nextN)


        for node in range(n):
            if node not in visited:
                bfs(node)
                output += 1

        return output
        