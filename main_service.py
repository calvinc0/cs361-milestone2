from flask import Flask, request, jsonify
import webbrowser

app = Flask(__name__)

@app.route('/launch_browser', methods=['POST'])
def launch_browser():
    try:
        # Get JSON data from the request
        data = request.get_json()
        command = data.get("command")
        url = data.get("url")

        # Validate the command and URL
        if not command or command != "open_url":
            return jsonify({"status": "error", "message": "Invalid command"}), 400

        if not url:
            return jsonify({"status": "error", "message": "URL is required"}), 400

        # Open the URL in the default web browser
        webbrowser.open(url)
        return jsonify({"status": "success", "message": f"Browser opened to {url}"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

