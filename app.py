from flask import Flask

from api.PlaceEndpoint import place_bp
from api.UserEndpoint import user_bp
from api.ReviewEndpoint import review_bp

app = Flask(__name__)

app.register_blueprint(place_bp)
app.register_blueprint(user_bp)
app.register_blueprint(review_bp)

if __name__ == '__main__':
    app.run(debug=True)