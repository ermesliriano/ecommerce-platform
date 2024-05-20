from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SERVICES = {
    "user_service": "http://user-service:5000",
    "product_service": "http://product-service:5000",
    "order_service": "http://order-service:5000",
    "payment_service": "http://payment-service:5000",
    "recommendation_service": "http://recommendation-service:5000"
}

@app.route('/<service>/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def gateway(service, path):
    if service in SERVICES:
        service_url = SERVICES[service]
        response = requests.request(
            method=request.method,
            url=f"{service_url}/{path}",
            headers={key: value for key, value in request.headers if key != 'Host'},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False
        )
        return (response.content, response.status_code, response.headers.items())
    else:
        return jsonify({"message": "Service not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
