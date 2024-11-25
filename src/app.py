from flask import Flask, jsonify, request
from src.blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    data = request.get_json()
    required_fields = ['sender', 'recipient', 'amount']
    if not all(field in data for field in required_fields):
        return "Missing values", 400
    index = blockchain.add_transaction(data['sender'], data['recipient'], data['amount'])
    return jsonify({'message': f'Transaction will be added to Block {index}'}), 201

@app.route('/mine', methods=['GET'])
def mine_block():
    blockchain.mine_block()
    return jsonify({'message': 'New block mined!', 'chain': blockchain.chain}), 200

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {'chain': [block.to_dict() for block in blockchain.chain], 'length': len(blockchain.chain)}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
