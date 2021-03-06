from flask import render_template, redirect, session, request, flash
from flask_app import app
import requests
import spotipy
from spotipy import SpotifyClientCredentials
# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fortnite/store")
def store():
    headers = {
        'TRN-api-key': 'd717a54c-5dea-4d9a-bbec-b458d29e8ec6'
    }
    # headers = {}
    r = requests.get('https://api.fortnitetracker.com/v1/store', headers=headers)
    print(r.json())
    return render_template("store.html", items= r.json())
    



@app.route("/search/new")
def search_form():
    return render_template("search_form.html")


@app.route("/search", methods=["POST"])
def search():
    search_term = request.form['search_term']
    cid = 'f93680415d4d48b8805a8334eb8e7e43'
    secret = 'ddc2931f3c1742c9a6215804570df7e1'
    auth_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    results= sp.search(search_term, type="track", limit=50)
    print(results)
    return render_template("tracks.html", tracks= results['tracks']['items'], search_term = search_term)
@app.route("/tracks")
def tracks():
    cid = 'f93680415d4d48b8805a8334eb8e7e43'
    secret = 'ddc2931f3c1742c9a6215804570df7e1'
    auth_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    results= sp.search("Beyonce", type="track", limit=50)
    print(results)
    return render_template("tracks.html", tracks= results['tracks']['items'], search_term = "Beyonce")
