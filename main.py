from fastapi import Depends, FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Form
from fastapi.encoders import jsonable_encoder

# from model import Movie, Recipe, Recipe_Ingredient, Ingredient
from model import Recipe, Recipe_Ingredient, Ingredient
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


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request, db: Session = Depends(get_database_session)):
    records = db.query(Recipe).all()
    return templates.TemplateResponse("index.html", {"request": request, "data": records})


@app.get("/recipe/{name}", response_class=HTMLResponse)
def read_item(request: Request, name: schema.Recipe.name, db: Session = Depends(get_database_session)):
    item = db.query(Recipe).filter(Recipe.id == name).first()

    # Join that gets the ingredients from a certain recipe
    ingredients = db.query(Ingredient).filter(Ingredient.id == Recipe_Ingredient.ingredient_id,
                                              Recipe.id == Recipe_Ingredient.recipe_id, Recipe.id == name).all()

    return templates.TemplateResponse("overview.html", {"request": request, "recipe": item, "data": ingredients})


''' This is the function to add recipes to the database'''


@app.post("/recipe/")
async def create_recipe(db: Session = Depends(get_database_session), ingredients: str = Form(...), name: schema.Recipe.name = Form(...), url: schema.Recipe.picture_url = Form(...), direction: schema.Recipe.direction = Form(...)):

    recipe = Recipe(name=name, picture_url=url, direction=direction)
    db.add(recipe)
    db.commit()
    db.refresh(recipe)

    ingredients = ingredients.split()

    for i in ingredients:
        # Add individual ingredients to database.
        ingredient = Ingredient(name=i)
        db.add(ingredient)
        db.commit()
        db.refresh(ingredient)

        # Associates ingredients and recipes
        ingredients = Recipe_Ingredient(
            recipe_id=recipe.id, ingredient_id=ingredient.id)
        db.add(ingredients)
        db.commit()
        db.refresh(ingredient)

    response = RedirectResponse('/recipe', status_code=303)
    return response


@app.patch("/recipe/{id}")
async def update_recipe(request: Request, id: int, db: Session = Depends(get_database_session)):
    requestBody = await request.json()
    recipe = db.query(Recipe).get(id)
    print(str(requestBody))

    name = requestBody['name']
    picture = requestBody['picture']
    direction = requestBody['direction']

    # This allows me to just add a picture instead of being required to fill out other attributes
    if len(str(name)) == 0 and len(str(direction)) == 0:
        recipe.picture_url = picture
    elif len(str(picture)) == 0 and len(str(direction)) == 0:
        recipe.name = name
    else:
        recipe.name = name
        recipe.picture_url = picture
        recipe.direction = direction

    db.commit()
    db.refresh(recipe)
    newRecipe = jsonable_encoder(recipe)
    return JSONResponse(status_code=200, content={
        "status_code": 200,
        "message": "success",
        "recipe": newRecipe
    })


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
