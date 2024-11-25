from blockchain import Blockchain

###########################################
##Brainstorm###############################
#There should be some provision such that only one blockchain is created.


blockchain=Blockchain()
b=blockchain.last_block
blockchain.mine_block()
c=blockchain.last_block
print(b.__dict__)
print(c.__dict__)
print(blockchain.chain)