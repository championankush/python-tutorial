# Project 4: Password Manager

A secure password manager application that helps users store, generate, and manage their passwords safely.

## 📋 Project Overview

This project creates a password manager that allows users to:
- Store encrypted passwords and account information
- Generate strong, random passwords
- Search and retrieve stored passwords
- Update and delete password entries
- Export/import password data
- Check password strength and security

## 🎯 Learning Objectives

By completing this project, you will learn:
- **Cryptography**: Implementing encryption and decryption
- **Security Best Practices**: Secure password handling and storage
- **Data Encryption**: Using cryptographic libraries
- **File Security**: Protecting sensitive data on disk
- **User Authentication**: Implementing master password protection
- **Data Validation**: Ensuring data integrity and security
- **Secure Input**: Handling sensitive user input safely

## 🚀 Features

### Core Features
- ✅ Store encrypted passwords and account details
- ✅ Generate strong, random passwords
- ✅ Search and retrieve stored passwords
- ✅ Update and delete password entries
- ✅ Master password protection
- ✅ Password strength checking
- ✅ Secure data storage and retrieval

### Advanced Features
- 🔐 AES encryption for data protection
- 🔑 Password generation with customizable criteria
- 📊 Password strength analysis
- 📤 Export/import functionality
- 🔍 Advanced search and filtering
- ⏰ Password expiration tracking
- 📱 Multi-platform compatibility

## 📁 Project Structure

```
04_password_manager/
├── README.md              # This file
├── password_manager.py    # Main application file
├── crypto_utils.py        # Encryption/decryption functions
├── password_generator.py  # Password generation logic
├── data_manager.py        # Data storage and retrieval
├── security_utils.py      # Security-related utilities
├── config.py              # Configuration settings
├── tests/                 # Test files
│   ├── test_crypto.py
│   ├── test_password_gen.py
│   └── test_data_manager.py
├── data/                  # Data storage
│   ├── passwords.enc      # Encrypted password database
│   └── config.json        # Application configuration
└── requirements.txt       # Dependencies
```

## 🔧 Implementation Details

### Security Architecture
- **Master Password**: PBKDF2 key derivation for master password
- **Data Encryption**: AES-256 encryption for stored passwords
- **Salt Generation**: Random salt for each encryption operation
- **Secure Storage**: Encrypted data stored in binary format

### Data Structure
Each password entry is structured as:
```python
{
    'id': 'unique_identifier',
    'title': 'Account Name',
    'username': 'user@example.com',
    'password': 'encrypted_password',
    'url': 'https://example.com',
    'notes': 'Additional notes',
    'created_date': '2023-12-01',
    'modified_date': '2023-12-01',
    'category': 'Social Media',
    'strength_score': 85
}
```

### Password Generation
The password generator creates strong passwords with:
- Uppercase and lowercase letters
- Numbers and special characters
- Configurable length and complexity
- Exclusion of similar characters (0/O, 1/l)

## 🎮 Usage Examples

### Basic Usage
```bash
# Run the application
python password_manager.py

# Add a new password entry
> add "Gmail" "user@gmail.com" "mypassword123"

# Generate a strong password
> generate --length 16 --special

# Search for passwords
> search "gmail"

# Get password details
> get "Gmail"

# Update a password
> update "Gmail" --password "newpassword456"
```

### Advanced Usage
```bash
# Add with additional details
> add "GitHub" "username" --url "https://github.com" --notes "Work account"

# Generate password with specific criteria
> generate --length 20 --uppercase --lowercase --numbers --special

# Export passwords
> export --format json --file passwords_backup.json

# Check password strength
> strength "mypassword123"

# List all passwords by category
> list --category "Social Media"
```

## 📊 Sample Output

```
=== Password Manager ===

Commands:
  add <title> <username> [password] [options]  - Add new password entry
  get <title>                                  - Get password details
  update <title> [options]                     - Update password entry
  delete <title>                               - Delete password entry
  list [options]                               - List all passwords
  search <query>                               - Search passwords
  generate [options]                           - Generate strong password
  strength <password>                          - Check password strength
  export [options]                             - Export passwords
  import <file>                                - Import passwords
  help                                         - Show this help
  quit                                         - Exit application

Options for add:
  --url <url>                                  - Website URL
  --notes <notes>                              - Additional notes
  --category <category>                        - Password category

Options for generate:
  --length <length>                            - Password length
  --uppercase                                  - Include uppercase letters
  --lowercase                                  - Include lowercase letters
  --numbers                                    - Include numbers
  --special                                    - Include special characters

> add "Gmail" "user@gmail.com" "MySecurePass123!"
Password entry added successfully!

> generate --length 16 --special
Generated password: K9#mP$vN2@qR7xYz

> get "Gmail"
📧 Gmail
👤 Username: user@gmail.com
🔑 Password: MySecurePass123!
🌐 URL: https://gmail.com
📝 Notes: Personal email account
📊 Strength: Strong (85/100)
📅 Created: 2023-12-01
📅 Modified: 2023-12-01

> strength "MySecurePass123!"
Password Strength Analysis:
Length: 16 characters ✅
Uppercase letters: 2 ✅
Lowercase letters: 8 ✅
Numbers: 3 ✅
Special characters: 1 ✅
No common patterns ✅
Overall Score: 85/100 (Strong)

> list
📋 All Passwords (3 entries):

1. Gmail (user@gmail.com) - Strong
2. GitHub (username) - Very Strong
3. Bank Account (user123) - Medium
```

## ✅ Success Criteria

- [ ] Application requires master password authentication
- [ ] Can add new password entries with encryption
- [ ] Can retrieve and decrypt stored passwords
- [ ] Generates strong, random passwords
- [ ] Implements secure data storage
- [ ] Provides password strength analysis
- [ ] Handles encryption/decryption errors
- [ ] Validates user input securely
- [ ] Shows helpful security messages
- [ ] Code follows security best practices

## 🚀 Bonus Features

1. **Password Categories**: Organize passwords by categories
2. **Password Expiration**: Track and alert about expired passwords
3. **Secure Sharing**: Share passwords securely with others
4. **Backup/Restore**: Automatic backup and restore functionality
5. **Password History**: Track password changes over time
6. **Two-Factor Authentication**: Support for 2FA codes
7. **Browser Integration**: Browser extension for auto-fill
8. **Cloud Sync**: Synchronize passwords across devices

## 💡 Implementation Tips

1. **Security First**: Never store passwords in plain text
2. **Strong Encryption**: Use industry-standard encryption algorithms
3. **Key Derivation**: Use PBKDF2 or similar for master password
4. **Secure Random**: Use cryptographically secure random generators
5. **Input Validation**: Validate all user input thoroughly
6. **Error Handling**: Don't leak sensitive information in error messages

## 🔗 Related Topics

- Cryptography and Encryption
- Security Best Practices
- Data Protection
- Password Security
- File I/O with Encryption
- User Authentication

## 📚 Additional Resources

- [Python Cryptography Library](https://cryptography.io/)
- [Password Security Best Practices](https://owasp.org/www-project-top-ten/)
- [AES Encryption](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
- [PBKDF2 Key Derivation](https://en.wikipedia.org/wiki/PBKDF2)

## 🔐 Security Considerations

### Important Security Notes:
1. **Master Password**: Choose a strong, memorable master password
2. **Backup Security**: Keep backups in a secure location
3. **Device Security**: Ensure your device is secure
4. **Regular Updates**: Keep the application updated
5. **No Cloud Storage**: This is a local password manager

### Security Features:
- AES-256 encryption for all stored data
- PBKDF2 key derivation for master password
- Secure random number generation
- No plain text storage of passwords
- Memory clearing after operations

---

**Ready to build your secure password manager? Let's get started!** 🔐 