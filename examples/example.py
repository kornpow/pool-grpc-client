from pathlib import Path
import json
from pprint import pprint
import os
import base64
from time import sleep
from datetime import datetime, timedelta

# Pip installed Modules
from poolgrpc import PoolClient
from poolgrpc.client import traderrpc
from protobuf_to_dict import protobuf_to_dict

credential_path = os.getenv("POOL_CRED_PATH", None)
if credential_path == None:
	credential_path = Path("/home/skorn/.pool/mainnet")
else:
	credential_path = Path(credential_path)

pool_ip = os.getenv("POOL_IP")
pool_port = os.getenv("POOL_PORT")

mac = str(credential_path.joinpath("pool.macaroon").absolute())
tls = str(credential_path.joinpath("tls.cert").absolute())

pool_ip_port = f"{pool_ip}:{pool_port}"


pool = PoolClient(
	pool_ip_port,
	macaroon_filepath=mac,
    cert_filepath=tls,
	# no_tls=True
)

import code
code.interact(local=dict(globals(), **locals())) 

# pool = PoolClient(
# 	pool_ip_port,
# 	macaroon_filepath=mac,
#     cert_filepath="pool.cert",
# 	# no_tls=True
# )

pool.get_info()

pool.batch_snapshots(b"",0)

order = traderrpc.Order(
    trader_key=bytes.fromhex("032d7f1b7f225dc6f6a6541112fa2f387bd6af5f5ae4cc02051c39df626a5510a6"),
    rate_fixed=200,
    amt=500000,
    min_units_match=5,
    max_batch_fee_rate_sat_per_kw=300
)

sidecar_bid = traderrpc.Bid(
    details=order,
    lease_duration_blocks=2016,
    version=4,
    min_node_tier=1,
)

pool.submit_order(bid=sidecar_bid)


order = traderrpc.Order(
    trader_key=bytes.fromhex("032d7f1b7f225dc6f6a6541112fa2f387bd6af5f5ae4cc02051c39df626a5510a6"),
    rate_fixed=700,
    amt=30_000_000,
    min_units_match=1,
    max_batch_fee_rate_sat_per_kw=1500
)

myask = traderrpc.Ask(
    details=order,
    lease_duration_blocks=2016,
    version=4,
)

pool.submit_order(ask=myask)