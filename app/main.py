from fastapi import FastAPI

app = FastAPI(
    title="Asistente Documental para Despachos Contables",
    version="0.1.0",
    description=(
        "API para dar seguimiento a solicitudes documentales "
        "por cliente y periodo mensual."
    ),
)


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "API del asistente documental funcionando",
        "status": "ok",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}