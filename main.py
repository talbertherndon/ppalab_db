from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


from routes.route_system import router as system_router
from routes.route_accounting import router as accounting_router


app = FastAPI()


# Add CORSMiddleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows the React app's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)



app.include_router(system_router, tags=["Systems"])
app.include_router(accounting_router, tags=["Accounting"])


