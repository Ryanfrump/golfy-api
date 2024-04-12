import uuid

from fastapi import FastAPI

from models.player import Player, CreatePlayerRequest 
from models.course import Course, CreateCourseRequest


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


@app.get("/course")
async def get_course() -> list[Course]:
    return courses.values()

@app.post("/course")
async def create_course(course_detail: CreateCourseRequest) -> uuid.UUID:
    course_id = uuid.uuid4()
    course = Course(id= course_id, name= course_detail.name, location= course_detail.location, holes= course_detail.holes)
    courses[course_id] = course
    return course_id

@app.put("/course/{course_id}")
async def update_player(course_id: uuid.UUID, new_course: CreateCourseRequest):
    updated_course = Course(id= course_id, name= new_course.name, location= new_course.location, holes= new_course.holes)
    courses[course_id] = updated_course

@app.delete("/course{course_id}")
async def delete_course(course_id: uuid.UUID):
    del courses[course_id]
