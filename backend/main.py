from fastapi import FastAPI
from pydantic import BaseModel
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserData(BaseModel):
    name: str
    gender: str
    dob: str
    parentage: str
    phonenumder: str


@app.post("/submit")
def submit_data(data: UserData):

    # Read existing data
    with open("data.json", "r") as file:
        users = json.load(file)

    # Add new data
    users.append(data.model_dump())

    # Save data
    with open("data.json", "w") as file:
        json.dump(users, file, indent=4)

    return {
        "success": True,
        "message": "Data submitted successfully!"
    }