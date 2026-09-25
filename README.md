# minbo

HBO Max API wrapper.

```python
from minbo import MinBO

client = MinBO()

show = client.show("b692705b-2f12-4a3d-ab4d-579124e0667c")
print(show.title, show.release_year, show.season_count)
for episode in show.seasons[0].episodes:
    print(episode.episode_number, episode.title)

# A show's page fills in one season at a time, so name the one you want.
season_two = client.show("ab553cdc-e15d-4597-b65f-bec9201fd2dd", 2)

movie = client.movie("92b085e4-764c-41ca-a46f-4d76a5b28642")
print(movie.title, movie.runtime, movie.maturity_rating)

# Downloading and parsing are separate, so a response can be kept as it was served.
page = client.movie.download("92b085e4-764c-41ca-a46f-4d76a5b28642")
movie = client.movie.load(page)
```

A page is HTML with everything it was built from written into a `__NEXT_DATA__`
script tag, and that tag names what it holds by position rather than by name. A
download keeps the tag as it was served and `load` reads the essentials out of
it into `ParsedShowModel` / `ParsedMovieModel`, which are generated from what
the recorded responses parse into.
