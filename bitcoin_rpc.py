from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Configuration
rpc_user = "rpcusername"  
rpc_password = "rpcpassword"  
rpc_host = "127.0.0.1"  
rpc_port = "38332"

# Connection string
rpc_url = f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"

# Connect to Bitcoin Core RPC
def connect_rpc():
    try:
        rpc_connection = AuthServiceProxy(rpc_url)
        return rpc_connection
    except JSONRPCException as e:
        print(f"An error occurred during connection: {e}")
        return None

# Balance
def get_balance(rpc_connection):
    try:
        balance = rpc_connection.getbalance()
        print(f"Wallet balance: {balance} BTC")
    except JSONRPCException as e:
        print(f"An error occurred while fetching balance: {e}")

# Generate a new receiving address
def get_new_address(rpc_connection):
    try:
        new_address = rpc_connection.getnewaddress()
        print(f"New Address: {new_address}")
        return new_address
    except JSONRPCException as e:
        print(f"An error occurred while generating address: {e}")
        return None

# Send a transaction
def send_to_address(rpc_connection, address, amount):
    try:
        txid = rpc_connection.sendtoaddress(address, amount)
        print(f"Transaction sent with txid: {txid}")
        return txid
    except JSONRPCException as e:
        print(f"An error occurred while sending transaction: {e}")
        return None


# Main logic
if __name__ == "__main__":
    print("Interacting with Bitcoin Core RPC...\n")
    rpc_connection = connect_rpc()
    if rpc_connection:
        new_address = get_new_address(rpc_connection)
        get_balance(rpc_connection)
        if new_address:
            send_to_address(rpc_connection, new_address, 0.000002)
        get_balance(rpc_connection)
