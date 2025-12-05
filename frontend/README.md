# Frontend

## Rodar em modo desenvolvimento

```bash
cd frontend
npm install
npm install vue-router
echo VITE_API_URL=http://localhost:5000 > .env
npm run dev
```

Abra `http://localhost:5173/` no navegador.

## Produção (opcional)

```bash
npm run build
npm run preview
```
