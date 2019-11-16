codex = 'qwertyuiopasdfghjklzxcvbnm '
alpha = 'abcdefghijklmnopqrstuvwxyz '


def encrypt_code(message, codex, alpha):
    encrypt_word = ""
    for word in message.lower():
        index = alpha.find(word)
        encrypt_word += codex[index]
    return encrypt_word


def decrypt_code(message, codex, alpha):
    decrypt_word = ""
    for word in message.lower():
        index = codex.find(word)
        decrypt_word += alpha[index]
    return decrypt_word


print(encrypt_code('I am a monkey in a big big world', codex, alpha))
print(decrypt_code('o qd q dgfatn of q wou wou vgksr', codex, alpha))

