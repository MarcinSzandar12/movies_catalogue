from ..tmdb_client import *
from unittest.mock import Mock
from ..main import app
import pytest

def test_get_movies_list(monkeypatch):
   mock_movies_list = ['Movie 1', 'Movie 2']

   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("requests.get", requests_mock)


   movies_list = get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list

def test_get_single_movie(monkeypatch):
   mock_movie = 'Best_Movie!'

   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movie
   monkeypatch.setattr("requests.get", requests_mock)

   movie = get_single_movie(movie_id="1")
   assert movie == mock_movie

def test_get_movie_images(monkeypatch):
   mock_images = ['image_1', 'image_2']

   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_images
   monkeypatch.setattr("requests.get", requests_mock)

   image = get_movie_images(movie_id="1")
   assert image == mock_images

def test_get_single_movie_cast(monkeypatch):
   mock_cast = 'Przykładowy opis'

   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_cast
   monkeypatch.setattr("requests.get", requests_mock)

   cast = get_single_movie_cast(movie_id="1")
   assert cast == mock_cast

####################################################################################

#@pytest.mark.parametrize("list_type", (
#  "popular", "top_rated", "now_playing","upcoming"
#))
#def test_homepage(monkeypatch, list_type):
#   api_mock = Mock(return_value={'results': []})
#   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

#   with app.test_client() as client:
#      response = client.get(f"/?list_type={list_type}")
#       assert response.status_code == 200
#       api_mock.assert_called_once_with(f"movie/{list_type}")