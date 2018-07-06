# Module to check all Validations to check websites and domain.

from flask_api import FlaskAPI
from cert_check import CertChecker

app = FlaskAPI(__name__)

@app.route("/<string:url>/", methods=['GET'])
def validate_certificate(url):
	if CertChecker(url).check() == True:
		return {'validatecertificate': url}

if __name__ == "__main__":
    app.run(debug=True)
