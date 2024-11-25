import hashlib

class ProofOfWork:
    @staticmethod
    def valid_proof(last_proof, proof, difficulty):
        """
        Validates the proof by ensuring the hash meets the required difficulty.
        """
        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:difficulty] == "0" * difficulty

    @staticmethod
    def compute_proof_of_work(last_proof, difficulty):
        """
        Computes the proof-of-work for a given difficulty level.
        """
        proof = 0
        while not ProofOfWork.valid_proof(last_proof, proof, difficulty):
            proof += 1
        return proof
