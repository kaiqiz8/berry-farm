from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # return 'Web Hook received', 200

    if request.method == 'POST':
        # Extract the payload (JSON data)
        payload = request.json

        # Get repository and pusher info (adjust keys based on your webhook payload structure)
        repo_name = payload.get('repository', {}.get('name', 'Unknown repository'))
        pusher_name = payload.get('pusher', {}.get('name', 'Unknown user'))

        print(f"New push to '{repo_name}' by {pusher_name}!")
        return jsonify({"message": "Webhook received and message printed!"}), 200
        # return 'Web Hook received', 200
    else:
        return jsonify({"error": "Invalid request method"}), 400

if __name__ == '__main__':
    # Run the server on all available interfaces and port 5000
    app.run(host='0.0.0.0', port=5000)