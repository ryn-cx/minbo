# minbo

HBO Max API wrapper.

```python
from minbo import MinBO

client = MinBO()

show = client.show("b692705b-2f12-4a3d-ab4d-579124e0667c")
series = show.props.page_props.mapped_data.idref14
print(series.title.full, series.release_year, series.number_of_seasons)
for episode in series.seasons[0].episodes:
    print(episode.episode_number, episode.title.full)

# A show's page fills in one season at a time, so name the one you want.
season_two = client.show("ab553cdc-e15d-4597-b65f-bec9201fd2dd", 2)

movie = client.movie("92b085e4-764c-41ca-a46f-4d76a5b28642")
feature = movie.props.page_props.mapped_data.idref14
print(feature.title.full, feature.runtime, feature.localized_rating.classifier)

# Downloading and parsing are separate, so a response can be kept as it was served.
page = client.movie.download("92b085e4-764c-41ca-a46f-4d76a5b28642")
movie = client.movie.load(page)
```
