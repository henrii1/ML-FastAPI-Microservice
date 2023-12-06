# Code is bugged, to be revised.
from fastapi import FastAPI, Response
from pydantic import BaseModel

from app_greedy import greedy_coin
from app_openai import submit_question, create_code
from app_wiki import get_wiki_keyword, get_wiki_page, get_wiki_summary, search_wiki_pages

app = FastAPI()

class Body(BaseModel):
    text: str

class Value(BaseModel):
    value: float


@app.get("/")
async def  root():
    return Response('<h1> THis is the landing page of the website. Try "/tasks" </h1>')

@app.get("/tasks")
async def tasks():
    return {"message": "use the 'docs' method on this page to checkout API's"}

@app.post("/generate-text", response_model= Body)
async def generate_text(body: Body):
    openai_question = submit_question(body.text)
    return openai_question

@app.post("/code", response_model = Body)
async def generate_code(body: Body):
    openai_code = create_code(body.text)
    return openai_code

@app.post("/coin", response_model = Value)
def change_coin(value: Value):
    get_coin = greedy_coin(Value.value)
    return get_coin

@app.post("/wiki-page", response_model = Body)
async def get_page(body: Body):
    page = get_wiki_page(body.text)
    return page

@app.post("/wiki-keyword", response_model= Body)
async def get_keyword(body: Body):
    keyword = get_wiki_keyword(body.text)
    return keyword



