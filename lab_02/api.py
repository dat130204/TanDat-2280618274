from flask import Flask, request, jsonify
from cipher.vigeneCipher import VigenereCipher
from cipher.playfair import PlayFairCipher
from cipher.caesar import CaesarCipher
from cipher.railfence import RailFenceCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# --- Vigenere ---
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    return jsonify({
        "encrypted_text": vigenere_cipher.vigenere_encrypt(data["plain_text"], data["key"])
    })

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    return jsonify({
        "decrypted_text": vigenere_cipher.vigenere_decrypt(data["encrypted_text"], data["key"])
    })

# --- Caesar ---
caesar_cipher = CaesarCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.get_json()
    return jsonify({
        "encrypted_text": caesar_cipher.encrypt_text(data["text"], int(data["key"]))
    })

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.get_json()
    return jsonify({
        "decrypted_text": caesar_cipher.decrypt_text(data["text"], int(data["key"]))
    })

# --- Playfair ---
playfair_cipher = PlayFairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_matrix():
    data = request.get_json()
    return jsonify({
        "playfair_matrix": playfair_cipher.create_playfair_matrix(data["key"])
    })

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    matrix = playfair_cipher.create_playfair_matrix(data["key"])
    return jsonify({
        "encrypted_text": playfair_cipher.playfair_encrypt(data["plain_text"], matrix)
    })

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    matrix = playfair_cipher.create_playfair_matrix(data["key"])
    return jsonify({
        "decrypted_text": playfair_cipher.playfair_decrypt(data["cipher_text"], matrix)
    })

# --- Rail Fence ---
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json()
    return jsonify({
        "encrypted_text": railfence_cipher.rail_fence_encrypt(data["plain_text"], int(data["key"]))
    })

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    return jsonify({
        "decrypted_text": railfence_cipher.rail_fence_decrypt(data["cipher_text"], int(data["key"]))
    })

# --- Transposition ---
transposition_cipher = TranspositionCipher()

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    return jsonify({
        "encrypted_text": transposition_cipher.encrypt(data["plain_text"], int(data["key"]))
    })

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    return jsonify({
        "decrypted_text": transposition_cipher.decrypt(data["cipher_text"], int(data["key"]))
    })

# --- Run server ---
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
