from fastapi import Depends, FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Form
from fastapi.encoders import jsonable_encoder

from model import Movie, Recipe, Recipe_Ingredient, Ingredient
import schema
from database import SessionLocal, engine
import model

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request, db: Session = Depends(get_database_session)):
#     records = db.query(Movie).all()
#     return templates.TemplateResponse("index.html", {"request": request, "data": records})


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request, db: Session = Depends(get_database_session)):
    records = db.query(Recipe).all()
    return templates.TemplateResponse("newIndex.html", {"request": request, "data": records})


# @app.get("/movie/{name}", response_class=HTMLResponse)
# def read_item(request: Request, name: schema.Movie.name, db: Session = Depends(get_database_session)):
#     item = db.query(Movie).filter(Movie.id == name).first()
#     return templates.TemplateResponse("overview.html", {"request": request, "movie": item})


@app.get("/recipe/{name}", response_class=HTMLResponse)
def read_item(request: Request, name: schema.Recipe.name, db: Session = Depends(get_database_session)):
    item = db.query(Recipe).filter(Recipe.id == name).first()

    # Adding ingredients to return with json:
    ingredients = db.query(Ingredient.name).filter(
        (Ingredient.id == Recipe_Ingredient.ingredient_id) & Recipe_Ingredient.recipe_id == Recipe.id).all()

    return templates.TemplateResponse("newOverview.html", {"request": request, "recipe": item, "data": ingredients})


# @app.post("/movie/")
# async def create_movie(db: Session = Depends(get_database_session), name: schema.Movie.name = Form(...), url: schema.Movie.url = Form(...), rate: schema.Movie.rating = Form(...), type: schema.Movie.type = Form(...), desc: schema.Movie.desc = Form(...)):
#     movie = Movie(name=name, url=url, rating=rate, type=type, desc=desc)
#     db.add(movie)
#     db.commit()
#     db.refresh(movie)
#     response = RedirectResponse('/movie', status_code=303)
#     return response


''' This is the function to add recipes to the database'''
# @app.post("/recipe/")
# async def create_recipe(db: Session = Depends(get_database_session), name: schema.Recipe.name = Form(...), url: schema.Recipe.picture_url = Form(...), instruction: schema.Recipe.instruction_id = Form(...)):

#     instruction = instruction()
#     recipe = Recipe(name=name, picture_url=url, instruction_id=instruction)

#     db.add(movie)
#     db.commit()
#     db.refresh(movie)
#     response = RedirectResponse('/movie', status_code=303)
#     return response


# @app.patch("/movie/{id}")
# async def update_movie(request: Request, id: int, db: Session = Depends(get_database_session)):
#     requestBody = await request.json()
#     movie = db.query(Movie).get(id)
#     movie.name = requestBody['name']
#     movie.desc = requestBody['desc']
#     db.commit()
#     db.refresh(movie)
#     newMovie = jsonable_encoder(movie)
#     return JSONResponse(status_code=200, content={
#         "status_code": 200,
#         "message": "success",
#         "movie": newMovie
#     })


@app.patch("/recipe/{id}")
async def update_recipe(request: Request, id: int, db: Session = Depends(get_database_session)):
    requestBody = await request.json()
    recipe = db.query(Recipe).get(id)
    recipe.name = requestBody['name']
    recipe.direction = requestBody['direction']
    db.commit()
    db.refresh(recipe)
    newRecipe = jsonable_encoder(recipe)
    return JSONResponse(status_code=200, content={
        "status_code": 200,
        "message": "success",
        "recipe": newRecipe
    })


# @app.delete("/movie/{id}")
# async def delete_movie(request: Request, id: int, db: Session = Depends(get_database_session)):
#     movie = db.query(Movie).get(id)
#     db.delete(movie)
#     db.commit()
#     return JSONResponse(status_code=200, content={
#         "status_code": 200,
#         "message": "success",
#         "movie": None
#     })


@app.delete("/recipe/{id}")
async def delete_movie(request: Request, id: int, db: Session = Depends(get_database_session)):
    recipe = db.query(Recipe).get(id)
    db.delete(recipe)
    db.commit()
    return JSONResponse(status_code=200, content={
        "status_code": 200,
        "message": "success",
        "recipe": None
    })
