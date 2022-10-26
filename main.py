from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

from game import Game

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

game = Game('유태혁', '백지오')


@app.get("/status")
async def status():
    return game.status


@app.post("/bet/{index}/")
async def make_bet(index: int, value: int = Body()):
    game.make_bet(index, value)


@app.post("/round/")
async def make_round():
    return game.make_round()


@app.post('/reset')
async def reset(name1: str, name2: str):
    global game
    game = Game(name1, name2)


@app.post('/more')
async def more(value: int = Body()):
    game.more(value)
