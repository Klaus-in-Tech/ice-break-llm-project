from typing import Union
from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from ice_breaker import ice_breaker_with
from pydantic import BaseModel


app = FastAPI()

load_dotenv()

# Initialize the Jinja2Templates object
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "message": "Hello, Klaus"}
    )


@app.post("/process")
async def process(name: str = Form(...)):
    try:
        summary, profile_pic_url = ice_breaker_with(name=name)
        if summary is None or profile_pic_url is None:
            raise ValueError("Either the summary or the profile picture is None")
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
    return JSONResponse(
        content={
            "summary_and_facts": summary.to_dict(),
            "picture_url": profile_pic_url,
        }
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
