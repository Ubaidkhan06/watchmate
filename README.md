# Complete Rest API developed by Django REST framework 

## IMDB clone api where users can access movies and see on which platform the stream, total reviews and average rating and review them. 

### http://127.0.0.1:8000/main/watchlist
- Admin can create movies, Normal User can access the movies.

### http://127.0.0.1:8000/main/watchlist/<movie_id>/
- Admin can Update and Destroy, normal user can access the individual movie.

### http://127.0.0.1:8000/main/platform
- Admin can create platform, normal User can access the platforms.

### http://127.0.0.1:8000/main/platform/<platform_id>/
- Admin can Update and Destroy, normal user can access the individual movie.

### http://127.0.0.1:8000/main/<movie_id>/review-create/
- Authenticated user can review a movie. 
- User can review a movie only once.

### http://127.0.0.1:8000/main/<movie_id>/review-list/
- All the reviews a single movie has

### http://127.0.0.1:8000/main/review/<review_id>/
- Individual review.
- Reviewer can Update Destroy the review

### http://127.0.0.1:8000/account/register/
- User can register their account.

### http://127.0.0.1:8000/account/login/
- Login url to get access token

### http://127.0.0.1:8000/account/logout/
- Logout url