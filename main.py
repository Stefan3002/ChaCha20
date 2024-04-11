import chacha

READ_SIZE = 64
key = '000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f'
int_key = chacha.prepare_key(key)
nonce = '000000000000004a00000000'
int_nonce = chacha.prepare_key(nonce)

def encrypt_file(file_path, out_name='output-encrypted'):
    total_bytes = 0
    print('Started the encryption...')
    with open(file_path, 'rb') as f:
        print('Opened the input file...')
        with open(out_name, 'wb') as out_f:
            while True:
                # Read the bytes of the file
                plaintext = f.read(READ_SIZE)
                total_bytes += len(plaintext)
                # Check for EOF
                if not plaintext:
                    break
                # Start encrypting the bytes as you read them
                res = chacha.chacha_encrypt_decrypt(int_key, 1, int_nonce, plaintext, mode='bytes')
                # Write the encrypted bytes to the output file
                out_f.write(res)
    print(f'Successfully encrypted the file and wrote {total_bytes} bytes')

def decrypt_file(file_path, out_name='output-decrypted'):
    total_bytes = 0
    print('Started the decryption...')
    with open(file_path, 'rb') as f:
        print('Opened the input file...')
        with open(out_name, 'wb') as out_f:
            while True:
                # Read the bytes of the file
                plaintext = f.read(READ_SIZE)
                total_bytes += len(plaintext)
                # Check for EOF
                if not plaintext:
                    break
                # Start encrypting the bytes as you read them
                res = chacha.chacha_encrypt_decrypt(int_key, 1, int_nonce, plaintext, mode='bytes')
                # Write the encrypted bytes to the output file
                out_f.write(res)
    print(f'Successfully decrypted the file and wrote {total_bytes} bytes')

encrypt_file('AI1_Plan.pdf')
decrypt_file('output-encrypted')