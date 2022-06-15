from fastapi import FastAPI
from routes.producto import producto


app = FastAPI(
    title="Mi primera API",
    description="Primer proyecto",
    version="0.0.1",
    openapi_tags=[{
        "name":"productos",
        "descripcion":"Productos routers",
    }]
)

app.include_router(producto)