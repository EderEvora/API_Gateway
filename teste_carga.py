import threading
import requests
import time

URL_BASE = 'http://localhost:5000'

ENDPOINTS = ['/users', '/products', '/orders']

resultados = []
lock = threading.Lock()

def fazer_requests(id_utilizador):
    endpoint = ENDPOINTS[id_utilizador % len(ENDPOINTS)]
    url = URL_BASE + endpoint

    start = time.time()
    try:
        resposta = requests.get(url, timeout=5)
        tempo = round((time.time() - start) * 1000, 2)
        with lock:
            resultados.append({
                'utilizador': id_utilizador,
                'endpoint': endpoint,
                'status': resposta.status_code,
                'tempo_ms': tempo,
                'erro': False
            })
        print(f"[Utilizador {id_utilizador}] {endpoint} → {resposta.status_code} ({tempo}ms)")
    except Exception as e:
        tempo = round((time.time() - start) * 1000, 2)
        with lock:
            resultados.append({
                'utilizador': id_utilizador,
                'endpoint': endpoint,
                'status': 0,
                'tempo_ms': tempo,
                'erro': True
            })
        print(f"[Utilizador {id_utilizador}] ERRO: {e}")

def run_teste(num_utilizadores):
    print(f"\n=== Teste de carga: {num_utilizadores} utilizadores ===\n")
    threads = []

    inicio_total = time.time()

    for i in range(num_utilizadores):
        t = threading.Thread(target=fazer_requests, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    duracao_total = round(time.time() - inicio_total, 2)

    total      = len(resultados)
    erros      = sum(1 for r in resultados if r['erro'])
    sucessos   = total - erros
    tempos     = [r['tempo_ms'] for r in resultados if not r['erro']]
    media      = round(sum(tempos) / len(tempos), 2) if tempos else 0

    print(f"\n=== Resultados ===")
    print(f"Total de requisições : {total}")
    print(f"Sucesso              : {sucessos}")
    print(f"Erros                : {erros}")
    print(f"Tempo médio          : {media} ms")
    print(f"Duração total        : {duracao_total} s")

# Alterar o number de utilizadores a simular
run_teste(50)
