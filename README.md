# HBNB Project - HolbertonSchool

## Dependencies
- Flask 3.0.3
- Email Validator 2.1.1
- Python 3.11
- Docker

## START SERVER
 - Run `docker compose up --build`
 - API listening to `http://localhost:8000`


## API ENDPOINTS

### USERS
- `POST /users`: Create a new user.
- `GET /users`: Retrieve a list of all users.
- `GET /users/{user_id}`: Retrieve details of a specific user.
- `PUT /users/{user_id}`: Update an existing user.
- `DELETE /users/{user_id}`: Delete a user.

### CITIES & COUNTRIES
- `GET /countries`: Retrieve all pre-loaded countries.
- `GET /countries/{country_code}`: Retrieve details of a specific country by its code.
- `GET /countries/{country_code}/cities`: Retrieve all cities belonging to a specific country.
- `POST /cities`: Create a new city.
- `GET /cities`: Retrieve all cities.
- `GET /cities/{city_id}`: Retrieve details of a specific city.
- `PUT /cities/{city_id}`: Update an existing city’s information.
- `DELETE /cities/{city_id}`: Delete a specific city.

### AMENITIES
- `POST /amenities`: Create a new amenity.
- `GET /amenities`: Retrieve a list of all amenities.
- `GET /amenities/{amenity_id}`: Retrieve detailed information about a specific amenity.
- `PUT /amenities/{amenity_id}`: Update an existing amenity’s information.
- `DELETE /amenities/{amenity_id}`: Delete a specific amenity.

### PLACES
- `POST /places`: Create a new place.
- `GET /places`: Retrieve a list of all places.
- `GET /places/{place_id}`: Retrieve detailed information about a specific place.
- `PUT /places/{place_id}`: Update an existing place’s information.
- `DELETE /places/{place_id}`: Delete a specific place.

### REVIEWS
- `POST /places/{place_id}/reviews`: Create a new review for a specified place.
- `GET /users/{user_id}/reviews`: Retrieve all reviews written by a specific user.
- `GET /places/{place_id}/reviews`: Retrieve all reviews for a specific place.
- `GET /reviews/{review_id}`: Retrieve detailed information about a specific review.
- `PUT /reviews/{review_id}`: Update an existing review.
- `DELETE /reviews/{review_id}`: Delete a specific review.