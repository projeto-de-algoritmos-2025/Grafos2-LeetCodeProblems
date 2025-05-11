#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    // Função para encontrar o pai de um nó no Union-Find
    int encontrarPai(int no, vector<int> &pai)
    {
        if (pai[no] == no)
            return no;
        return pai[no] = encontrarPai(pai[no], pai);
    }

    // Função para construir a MST e retornar o peso total
    int encontrarMST(int n, vector<vector<int>> &arestas, int arestaExcluida, int arestaIncluida)
    {
        vector<int> pai(n);
        iota(pai.begin(), pai.end(), 0); // Inicializa cada nó como seu próprio pai
        int pesoTotal = 0;

        // Se queremos forçar uma aresta a entrar, une ela primeiro
        if (arestaIncluida != -1)
        {
            int u = arestas[arestaIncluida][0];
            int v = arestas[arestaIncluida][1];
            int peso = arestas[arestaIncluida][2];
            int paiU = encontrarPai(u, pai);
            int paiV = encontrarPai(v, pai);
            if (paiU != paiV)
            {
                pai[paiU] = paiV;
                pesoTotal += peso;
            }
        }

        // Agora processa todas as outras arestas
        for (int i = 0; i < arestas.size(); i++)
        {
            if (i == arestaExcluida)
                continue;
            int u = arestas[i][0];
            int v = arestas[i][1];
            int peso = arestas[i][2];
            int paiU = encontrarPai(u, pai);
            int paiV = encontrarPai(v, pai);
            if (paiU != paiV)
            {
                pai[paiU] = paiV;
                pesoTotal += peso;
            }
        }

        // Confere se o grafo está conectado
        int componentes = 0;
        for (int i = 0; i < n; i++)
        {
            if (pai[i] == i)
                componentes++;
        }
        if (componentes > 1)
            return 1e9; // Valor bem alto (infinito)

        return pesoTotal;
    }

    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>> &arestas)
    {
        // Adiciona o índice original da aresta
        for (int i = 0; i < arestas.size(); i++)
        {
            arestas[i].push_back(i);
        }

        // Ordena as arestas por peso
        sort(arestas.begin(), arestas.end(), [](vector<int> &a, vector<int> &b)
             { return a[2] < b[2]; });

        // Calcula o peso da MST original
        int pesoOriginal = encontrarMST(n, arestas, -1, -1);

        vector<int> criticas, pseudoCriticas;

        // Testa cada aresta
        for (int i = 0; i < arestas.size(); i++)
        {
            // Testa se é crítica (removendo a aresta)
            int pesoSemAresta = encontrarMST(n, arestas, i, -1);
            if (pesoSemAresta > pesoOriginal)
            {
                criticas.push_back(arestas[i][3]);
            }
            else
            {
                // Testa se é pseudo-crítica (forçando a inclusão)
                int pesoComAresta = encontrarMST(n, arestas, -1, i);
                if (pesoComAresta == pesoOriginal)
                {
                    pseudoCriticas.push_back(arestas[i][3]);
                }
            }
        }

        return {criticas, pseudoCriticas};
    }
};
