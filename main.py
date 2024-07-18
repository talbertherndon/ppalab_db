from fastapi import FastAPI, HTTPException

from routes.route_system import router as system_router
from routes.route_accounting import router as accounting_router


app = FastAPI()

app.include_router(system_router, tags=["Systems"])
app.include_router(accounting_router, tags=["Accounting"])


