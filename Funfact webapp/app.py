import requests
import random
from bs4 import BeautifulSoup
from flask import Flask,render_template,request



app=Flask(__name__)


@app.route("/",methods=["GET","POST"])
def home():

        url="https://www.thefactsite.com/1000-interesting-facts/"

        response=requests.get(url)

        pag_content=response.content

        soup=BeautifulSoup(pag_content,"html.parser")

        x=soup.find_all(class_="list")

        l=[i.get_text() for i in x]

        fact=None
        
        if request.method=="POST":
            fact= random.choice(l)

            
        return render_template("index.html",fact=fact)
    
if __name__=="__main__":
    app.run(debug=True)
