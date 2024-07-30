from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


from routes.route_system import router as system_router
from routes.route_runs import router as runs_router
from routes.route_workloads import router as workloads_router

app = FastAPI()


# Add CORSMiddleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","https://ipca-lab-reservation-system.apps1-fm-int.icloud.intel.com"],  # Allows the React app's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)



app.include_router(system_router, tags=["Systems"])
app.include_router(runs_router, tags=["Runs"])
app.include_router(workloads_router, tags=["Workloads"])



