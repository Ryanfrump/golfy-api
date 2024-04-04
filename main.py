import uuid

from fastapi import FastAPI

from models.player import Player
from models.course import Course


app = FastAPI()

players: dict[uuid.UUID, Player] = {}
courses: dict[uuid.UUID, Course] = {}

@app.get("/player")

#@app.post("/player")

#@app.put("/player/{player_id}")

#@app.delete("/player/{player_id}")


#@app.get("/course")

#@app.post("/course")

#@app.put("/course/{course_id}")

#@app.delete("/course{course_id}")
