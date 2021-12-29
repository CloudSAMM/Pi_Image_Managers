from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .image_manager import ImageInterface
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/query")
async def query(
    bucket: str = None, year: str = None, month: str = None, day: str = None
):
    prefix = ImageInterface.create_prefix(year, month, day)
    return ImageInterface.get_images(bucket, prefix)


@app.get("/image/{bucket}/{date}/{image}")
async def show_image(bucket: str, date: str, image: str):
    try:
        signed_url = ImageInterface.generate_url(bucket, f"{date}/{image}")
        header = {"s3url": signed_url}
        return JSONResponse(header, headers=header)
    except Exception as e:
        return JSONResponse({"error", str(e)}, status_code=401)



@app.get("/")
async def token():

    return {"ok": True}
