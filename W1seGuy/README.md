# W1seGuy
## Description

This room focuses on XOR encryption and decryption, making it an excellent starting point for beginners to understand the fundamentals of XOR-based cryptography.

The challenge involves a Python program running on a server that encrypts text using the XOR method. Your task is to decrypt the provided encrypted text to uncover the flag.
### XOR Encryption

XOR encryption is a simple yet powerful method of encrypting data. Here's a basic example:

```python
Plain Text      : 10101010
Key             : 11110000
--------------------------
Encrypted Text  : 01011010
```

### XOR Decryption

The beauty of XOR encryption lies in its reversibility. If you have two of the three components (Plain Text, Key, or Encrypted Text), you can derive the third using the XOR operation.
#### Example 1:

```python
Encrypted Text  : 01011010
Plain Text      : 10101010
--------------------------
Key             : 11110000
```

#### Example 2:
```python
Key             : 11110000
Encrypted Text  : 01011010
--------------------------
Plain Text      : 10101010
```

## Solution

The provided Python script uses a flag in the format THM{example_flag} as the plaintext and a 5-character key for encryption. By leveraging the known structure of the flag (starting with THM{ and ending with }), we can deduce the key and decrypt the flag.

### Step 1: Determine the Key

#### First 4 Characters of the Key:
Use the known plaintext **THM{** and the corresponding encrypted text to derive the first 4 characters of the key.

```python
Plain Text      : THM{
Encrypted Text  : dqdq
--------------------------
Key (first 4)   : (Derived using XOR)
```

#### Last Character of the Key:

Use the known plaintext **}** and the corresponding encrypted text to derive the last character of the key.

```python
Plain Text      : }
Encrypted Text  : b
--------------------------
Key (last char) : (Derived using XOR)
```

### Step 2: Decrypt the Flag
Once the key is fully determined, use it to decrypt the encrypted text and reveal the flag.