class minCostMaxFlowBf:
    class Edge:
        def __init__(self, v, cap, cost, rev):
            self.to = v
            self.cap = cap
            self.cost = cost
            self.rev = rev
            self.f = 0
    def createGraph(self, n):
        graph = []
        for i in range(n):
            graph.append([])
        return graph
    def addEdge(self, graph, s, t, cap, cost):
        graph[s].append(self.Edge(t, cap, cost, len(graph[t])))
        graph[t].append(self.Edge(s, 0, -cost, len(graph[s])-1))
    def bellmanFord(self, graph, s, dist, prevnode, prevedge, curflow):
        n = len(graph)
        for i in range(n):
            dist[i] = 2000000000
        dist[s] = 0
        curflow[s] = 2000000000
        inqueue = [False]*n
        q = [0]*n
        q[0]=s
        qt,qh=1,0
        while((qh-qt)%n!=0):
            u = q[qh%n]
            inqueue[u] = False
            for i in range(len(graph[u])):
                e = graph[u][i]
                if e.f>=e.cap:
                    continue
                v = e.to
                ndist = dist[u] + e.cost
                if dist[v] > ndist:
                    dist[v] = ndist
                    prevnode[v] = u
                    prevedge[v] = i
                    curflow[v] = min(curflow[u], e.cap - e.f)
                    if (not inqueue[v]):
                        inqueue[v] = True
                        q[qt%n] = v
                        qt+=1
            qh+=1
    def minCostFlow(self, graph, s, t, maxf):
        n = len(graph)
        dist = [0] * n
        curflow = [0] * n
        prevedge = [0] * n
        prevnode = [0] *n
        
        flow, flowCost = 0, 0
        while(flow<maxf):
            self.bellmanFord(graph, s, dist, prevnode, prevedge, curflow)
            if dist[t] == 2000000000:
                break
            df = min(curflow[t], maxf - flow)
            flow += df
            v = t
            while v!=s:
                e = graph[prevnode[v]][prevedge[v]]
                e.f += df
                graph[v][e.rev].f -= df
                flowCost += df * e.cost
                v = prevnode[v]
        return [flow, flowCost]
