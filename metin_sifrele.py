def Encrypt(stringParam: str, passwordParam: int) -> str:
    
    """Metni verilen sabit anahtar (15) ile XOR işlemi kullanarak şifreler."""
    newString = ""
    
    for character in stringParam:
        char_value = ord(character)
        newCharacter_value = char_value ^ passwordParam
        newString += chr(newCharacter_value)
    
    return newString


def Decrypt(stringParam: str, passwordParam: int) -> str:
    
    """Şifrelenmiş metni verilen sabit anahtar (15) ile çözer."""
    newString = ""
    for character in stringParam:
        char_value = ord(character)
        # Şifre çözme işlemi, şifreleme ile aynıdır (XOR özelliği)
        originalCharacter_value = char_value ^ passwordParam
        newString += chr(originalCharacter_value)
    
    return newString




# 1. Sabit Parola (Anahtar) Değeri
password = 15  

# 2. Kullanıcıdan alınan şifrelenecek String
string_to_process = input("Lütfen şifrelemek istediğiniz metni (string) girin: ")

print("-" * 30)
print(f"Kullanılan Sabit Anahtar: {password}")
print("-" * 30)

# Şifreleme İşlemi
encryptedString = Encrypt(string_to_process, password)
print(f"Orijinal Metin: '{string_to_process}'")
print(f"Şifrelenmiş Metin: '{encryptedString}'")

# Şifre Çözme İşlemi
decryptedString = Decrypt(encryptedString, password)
print(f"Şifresi Çözülmüş Metin: '{decryptedString}'")