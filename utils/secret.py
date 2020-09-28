import bcrypt
from setting import RSA_PRIVATE_KEY_PATH

def generate_hash_password(self, password):
    password_hash = bcrypt.hashpw(password.encode('utf-8'),
                                      bcrypt.gensalt())
    return password_hash

def is_hash_matches_password(self, password, password_hash):
    return bcrypt.checkpw(password.encode('utf-8'), password_hash)

def rsa_decrypt(self, field, private_key):
    if isinstance(field, str):
        decode_value = base64.b64decode(field)
        value = rsa.decrypt(decode_value, self._rsa_private_key)
        return value.decode('utf-8')
    return None

def get_rsa_private_key(key_file_path=RSA_PRIVATE_KEY_PATH):
    with open(key_file_path) as key_file:
        key_data = key_file.read()
        return rsa.PrivateKey.load_pkcs1(key_data)
