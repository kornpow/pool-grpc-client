from pathlib import Path
import json
from pprint import pprint
import os
import base64
from time import sleep
from datetime import datetime, timedelta

# Pip installed Modules
from poolgrpc import PoolClient
from protobuf_to_dict import protobuf_to_dict

credential_path = os.getenv("POOL_CRED_PATH", None)
if credential_path == None:
	credential_path = Path("/home/skorn/.pool/mainnet")
else:
	credential_path = Path(credential_path)

pool_ip = "192.168.1.58"

mac = str(credential_path.joinpath("pool.macaroon").absolute())
tls = str(credential_path.joinpath("tls.cert").absolute())

pool = PoolClient(
	f"{pool_ip}:12010",
	macaroon_filepath=mac,
	cert_filepath=tls
)

pool.get_info()