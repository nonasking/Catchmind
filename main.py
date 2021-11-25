from flask import Flask, render_template, request, redirect, send_file
from bs4 import BeautifulSoup
import requests
import random
from operator import itemgetter

app = Flask("CatchMind")

db=[]

@app.route("/")
def index():
  def extract_animals():
    url="https://rich-useful.tistory.com/19"
    result=requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    animals_soup=soup.find("div", {"class": "jb-article"}).find_all("b")
    animals=[]
    for animal in animals_soup:
      animal=animal.get_text(strip=1)
      animals.append(animal)
    animal=random.choice(animals)
    if animal in db:
      animals.remove(animal)
      animal=random.choice(animals)
    else:
      db.append(animal)
    return animal
  animal=extract_animals()
  print(db)
  return render_template("index.html", animal=animal)

@app.route("/reselect")
def reselect():
  return redirect("/")

app.run(host="0.0.0.0")
