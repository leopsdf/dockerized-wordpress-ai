# Dockerized WordPress + IA API

Sobe um ambiente local com WordPress (8080) e API de IA (8000).

## Subir o ambiente
```bash
docker compose up -d --build
```

## Acessos
- WordPress: http://localhost:8080
- API de IA: http://localhost:8000/predict?text=serviço%20público

## Integração do Plugin
1. Instale o plugin `INCLUA – Demo` no WordPress.
2. Em **INCLUA Demo**, configure `URL base da API` = `http://aiapi:8000/` (dentro do *compose*, o WordPress pode acessar o serviço `aiapi` pelo nome do container). Para testar via navegador, use `http://localhost:8000/`.
3. Crie uma página e insira: `[inclua_quote text="inclusão e equidade"]`.

## Dicas
- Para persistir dados do WP, utilize os volumes já configurados (`wp_data`).

## Licença
MIT
