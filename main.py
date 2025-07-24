from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

@app.get("/hello")
def read_hello(request: Request):
    accept_headers = request.headers.get("Accept")
    return JSONResponse({"message": "Hello World"}, status_code=200)


class WelcomeRequest(BaseModel):
    name: str


@app.get("/welcome")
def welcome_user(request: WelcomeRequest):
    return {f"Bienvenue {request.name}"}

class StudentsRequest(BaseModel):
    reference: str
    firstName: str
    lastName: str
    age: int

@app.post("/students")
def post_students(request: Request, request_body: StudentsRequest):
    created_headers = request.headers.get("Created")
        return JSONResponse({f"Reference {request_body.reference}",
                             f"FirstName {request_body.firstname}",
                             f"LastName {request_body.lastName}",
                             f"Age {request_body.age}"},
                            status_code=200
                             )
