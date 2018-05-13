from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto import Random
import base64

random_generator = Random.new().read

# used to generate a keypair which contain a public and private key
rsa = RSA.generate(1024, random_generator)
prikey = rsa.exportKey()
pubkey = rsa.publickey().exportKey()

# sign with prikey
message = b'Hello World'
rsakey = RSA.importKey(prikey)
signer = Signature_pkcs1_v1_5.new(rsakey)
digest = SHA256.new()
digest.update(message)
sign = signer.sign(digest)
signature = base64.b64encode(sign)

# verify
rsakey = RSA.importKey(pubkey)
verifier = Signature_pkcs1_v1_5.new(rsakey)
digest = SHA256.new()
# Assumes the data is base64 encoded to begin with
digest.update(message)
is_verify = signer.verify(digest, base64.b64decode(signature))
print(is_verify)
