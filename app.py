from flask import Flask, request, jsonify

app = Flask(__name__)

# مفتاح سري خاص فيك (غيره بكلمة قوية)
SECRET_KEY = "MY_SECRET_KEY_2025"

@app.route("/myendpoint", methods=["GET"])
def private_endpoint():
    auth = request.headers.get("Authorization")
    if auth != f"Bearer {SECRET_KEY}":
        return jsonify({"error": "🚫 Unauthorized"}), 401
    
    return jsonify({
        "message": "✅ مرحباً! هذا Endpoint خاص بك فقط",
        "status": "success"
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
