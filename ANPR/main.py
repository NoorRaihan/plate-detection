from fastapi import FastAPI, File, UploadFile
from detect import read_image
from pydantic import BaseModel
import uuid
import shutil

#init fastapi
app = FastAPI()

@app.get('/')
async def index():
    return {"message" : "API for CSC508"}


@app.post('/plate')
async def uploadfile(file: UploadFile = File(...)):
    file_content = file.file
    
    file_ext = file.filename.split(".")
    uid = str(uuid.uuid4())
    new_name = uid + "."+file_ext[1]

    with open("uploads/"+new_name, "wb") as buffer:
        shutil.copyfileobj(file_content, buffer)

    plate = read_image("uploads/"+new_name)
    return {
            "respCode": 00000,
            "respMsg" : "success",
            "data" : plate
            }
