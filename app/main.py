from fastapi import FastAPI
from app.database.connection import engine
from app.models import task as task_model
from app.models import user as user_model
from app.routes import task as task_route
from app.routes import auth as auth_route

task_model.Base.metadata.create_all(bind=engine)
user_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_route.router, prefix='/api')
app.include_router(task_route.router, prefix='/api')

@app.get("/")
def read_root():
    return {"message": "Hello World!"}