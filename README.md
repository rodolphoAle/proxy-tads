# Proxy-TADS

Sistema proxy para requisições externas, com fila, worker, cache e arquitetura modular em Flask.

## Estrutura de Pastas

```
proxy-tads/
│
├── app.py                # Ponto de entrada principal
├── Dockerfile            # Build do container Docker
├── requiriments.txt      # Dependências Python
│
├── app/
│   ├── __init__.py       # Factory do Flask (create_app)
│   ├── config.py         # Configurações do projeto
│
├── routes/
│   ├── routes.py         # Rotas principais
│   └── __init__.py       # (opcional para blueprints)
│
├── services/
│   ├── worker.py         # Worker (thread) para processar fila
│   ├── request_queue.py  # Fila de requisições (singleton)
│   ├── request_command.py# Comando de requisição
│   ├── cache.py          # Sistema de cache (singleton)
│
└── ...
```

## Como Executar Localmente

1. Instale as dependências:

   ```bash
   pip install -r requiriments.txt
   ```
2. Execute o projeto:

   ```bash
   python app.py
   ```
3. Acesse em [http://localhost:5000](http://localhost:5000)

## Como Executar com Docker

1. Build da imagem:

   ```bash
   docker build -t proxy-tads .
   ```
2. Rode o container:

   ```bash
   docker run -p 5000:5000 proxy-tads
   ```
3. Acesse em [http://localhost:5000](http://localhost:5000)

## Exemplos de Uso

- Endpoint principal:

  ```
  GET /proxy/score/<cpf>
  ```

  Retorna o resultado do processamento, usando cache se disponível.

## Observações

- Não recomendado para produção sem ajustes de segurança e escalabilidade.
- Para produção, utilize um servidor WSGI (ex: Gunicorn) e configure variáveis de ambiente.

## Arquitetura de Serviços

* **Flask Factory** : Inicialização via `create_app` para facilitar testes e extensões.
* **Fila de Requisições** : Implementada com padrão Singleton, garantindo apenas uma instância.
* **Worker** : Thread dedicada para processar requisições da fila, respeitando rate limit.
* **Cache** : Sistema LRU com TTL, também Singleton, para respostas rápidas e evitar processamento desnecessário.
* **Rotas** : Separadas em módulos, podendo ser organizadas como blueprints.

## Padrões e Princípios Aplicados

* **Singleton** : Para fila e cache, evitando múltiplas instâncias e problemas de concorrência.
* **Separation of Concerns** : Cada módulo tem responsabilidade única (rotas, worker, cache, fila).
* **SOLID** :
* **Single Responsibility Principle** : Cada classe/módulo faz apenas uma coisa.
* **Open/Closed Principle** : Fácil de estender (ex: adicionar novos tipos de worker ou cache).
* **Dependency Inversion** : Uso de injeção via factory e importação de serviços.
* **Clean Code** : Nomes claros, modularização, tratamento de erros, uso de docstrings e comentários explicativos.
* **Thread-Safe** : Uso de locks e filas do Python para garantir segurança em concorrência.

## Observações

* Para produção, utilize um servidor WSGI (ex: Gunicorn) e configure variáveis de ambiente.
