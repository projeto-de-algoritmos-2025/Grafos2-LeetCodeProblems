import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        #Construir o grafo (lista de adjacência)
        grafo = defaultdict(list)
        for u, v, w in times:
            grafo[u].append((v, w))

        #Dijkstra a partir do nó k
        min_heap = [(0, k)]  # (tempo acumulado, nó)
        tempos = {}  # Dicionário para armazenar o tempo mínimo para cada nó

        while min_heap:
            tempoAtual, no = heapq.heappop(min_heap)

            if no in tempos:
                continue  # Já visitamos esse nó

            tempos[no] = tempoAtual

            for vizinho, peso in grafo[no]:
                if vizinho not in tempos:
                    heapq.heappush(min_heap, (tempoAtual + peso, vizinho))

        #Conferir se todos os nós foram alcançados
        if len(tempos) != n:
            return -1

        #Retornar o maior tempo entre os nós alcançados
        return max(tempos.values())
