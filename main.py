from chain import Blockchain

if __name__ == "__main__":
    print('READY')
    
    for x in range(1, 10):
        bc = Blockchain()
        print(x, " => ", bc.chain)
        