from fastapi import APIRouter,File, UploadFile
from app.index.indexing_pipeline import Pipeline
insert_data_router = APIRouter()


@insert_data_router.post("/insert", response_model=str)
def insert_data(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    if Pipeline().run(file.filename) ==0:
        return f"Successfully inserted {file.filename}"
    else:
        return f"Insertion failed: {file.filename}"