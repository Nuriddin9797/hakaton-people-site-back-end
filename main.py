import os
from fastapi import FastAPI, HTTPException
from starlette.responses import FileResponse
from routes.likes import likes_router
from routes.web_sockets import web_socket_router
from routes.files import files_router
from routes.programming import programming_router
from routes.jobs import jobs_router
from routes.users import users_router
from routes.income import income_router
from routes.application import application_router
from routes.results_routes import router_result
from routes.answer_routes import router_answer
from routes.categories_routes import router_categories
from routes.question_routes import router_question
from routes.admin_routes import admin_router
from routes.login import login_router
from routes.final_result_routes import routes_final_result

app = FastAPI(docs_url='/')


app.include_router(login_router)
app.include_router(admin_router)
app.include_router(users_router)
app.include_router(jobs_router)
app.include_router(programming_router)
app.include_router(application_router)
app.include_router(likes_router)
app.include_router(income_router)
app.include_router(router_categories)
app.include_router(router_question)
app.include_router(router_answer)
app.include_router(router_result)
app.include_router(routes_final_result)
app.include_router(web_socket_router)
app.include_router(files_router)


@app.get('/files/{fileName}')
async def get_file(fileName: str):
    path = f"./files/{fileName}"
    if os.path.isfile(path):
        return FileResponse(path)
    else:
        raise HTTPException(400, "Not Found")