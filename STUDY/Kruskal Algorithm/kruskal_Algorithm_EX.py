class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        answer = 0
        parent = [0] * (len(points) + 1)
        
        # 두 점 사이의 거리 = 맨해튼 거리
        def manhattan_distance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            
            return abs(x1 - x2) + abs(y1 - y2)
    
        # 특정 원소가 속한 집합 찾기
        def find_parent(parent, x):
            # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
            if parent[x] != x:
                parent[x] = find_parent(parent, parent[x])
                
            return parent[x]
        
        # 두 원소가 속한 집합을 합치기
        def union_parent(parent, a, b):
            a = find_parent(parent, a)
            b = find_parent(parent, b)
            if a < b:
                parent[b] = a
            else:
                parent[a] = b
                
        # 모든 간선에 대한 정보를 edges에 담기
        edges = []

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                edges.append((manhattan_distance(points[i], points[j]), i + 1, j + 1))

        edges.sort() # 맨해튼 거리가 짧은 순으로 오름차순 정렬
        
        # 부모 테이블 상에서, 부모를 자기 자신으로 초기화
        for i in range(1, len(points) + 1):
            parent[i] = i
        
        for edge in edges:
            cost, a, b = edge
            
            # 싸이클이 발생하지 않는 경우에만 union 실행
            if find_parent(parent, a) != find_parent(parent, b):
                union_parent(parent, a, b)
                answer += cost
            
        return 
