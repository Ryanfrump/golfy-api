import uuid

from fastapi import FastAPI

from models.player import Player, CreatePlayerRequest, PlayerResponse
from models.course import Course


app = FastAPI()

players: dict[uuid.UUID, Player] = {}
courses: dict[uuid.UUID, Course] = {}

@app.get("/player")
async def get_players() -> list[Player]:
    return players.values()

@app.post("/player")
async def create_player(player_detail: CreatePlayerRequest) -> uuid.UUID:
    player_id = uuid.uuid4()
    player = Player(id=player_id, name=player_detail.name, handicap=player_detail.handicap)
    players[player.id] = player
    return player.id

@app.put("/player/{player_id}")
async def update_player(player_id: uuid.UUID, new_player: CreatePlayerRequest):
    updated_player = Player(id=player_id, name=new_player.name, handicap=new_player.handicap)
    players[player_id] = updated_player


@app.delete("/player/{player_id}")
async def delete_player(player_id: uuid.UUID):
    del players[player_id]


#@app.get("/course")

#@app.post("/course")

#@app.put("/course/{course_id}")

#@app.delete("/course{course_id}")
