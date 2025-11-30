import hashlib
import sys
import time

def hash_password(password, algorithm):
    """Convert a password to its hash."""
    if algorithm == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    else:
        return None

def crack_hash(target_hash, algorithm, wordlist_path):
    """Try to crack a hash using a wordlist."""
    print(f"\nTarget hash: {target_hash}")
    print(f"Algorithm: {algorithm}")
    print(f"Wordlist: {wordlist_path}")
    print("\nCracking...\n")
    
    start_time = time.time()
    attempts = 0
    
    try:
        with open(wordlist_path, 'r', encoding='latin-1') as file:
            for line in file:
                password = line.strip()
                attempts += 1
                
                # Hash the password and compare
                hashed = hash_password(password, algorithm)
                
                if hashed == target_hash:
                    end_time = time.time()
                    print(f"✓ PASSWORD FOUND: {password}")
                    print(f"  Attempts: {attempts:,}")
                    print(f"  Time: {end_time - start_time:.2f} seconds")
                    return password
                
                # Show progress every 1 million attempts
                if attempts % 1000000 == 0:
                    print(f"  Tried {attempts:,} passwords...")
    
    except FileNotFoundError:
        print(f"Error: Wordlist file not found at {wordlist_path}")
        return None
    
    end_time = time.time()
    print(f"✗ Password not found")
    print(f"  Attempts: {attempts:,}")
    print(f"  Time: {end_time - start_time:.2f} seconds")
    return None

def generate_hash(password, algorithm):
    """Generate a hash for testing."""
    hashed = hash_password(password, algorithm)
    print(f"\nPassword: {password}")
    print(f"Algorithm: {algorithm}")
    print(f"Hash: {hashed}")
    return hashed

def main():
    print("=" * 50)
    print("HASH CRACKER (Educational)")
    print("=" * 50)
    
    # Check command line arguments
    if len(sys.argv) < 2:
        print("\nUsage:")
        print("  Crack a hash:")
        print("    python cracker.py crack <hash> <algorithm>")
        print("    Example: python cracker.py crack 482c811da5d5b4bc6d497ffa98491e38 md5")
        print("\n  Generate a hash (for testing):")
        print("    python cracker.py generate <password> <algorithm>")
        print("    Example: python cracker.py generate password123 md5")
        print("\n  Algorithms: md5, sha256")
        return
    
    command = sys.argv[1].lower()
    
    if command == 'crack':
        if len(sys.argv) < 4:
            print("Error: Missing arguments")
            print("Usage: python cracker.py crack <hash> <algorithm>")
            return
        
        target_hash = sys.argv[2].lower()
        algorithm = sys.argv[3].lower()
        wordlist_path = 'data/rockyou.txt'
        
        if algorithm not in ['md5', 'sha256']:
            print("Error: Algorithm must be 'md5' or 'sha256'")
            return
        
        crack_hash(target_hash, algorithm, wordlist_path)
    
    elif command == 'generate':
        if len(sys.argv) < 4:
            print("Error: Missing arguments")
            print("Usage: python cracker.py generate <password> <algorithm>")
            return
        
        password = sys.argv[2]
        algorithm = sys.argv[3].lower()
        
        if algorithm not in ['md5', 'sha256']:
            print("Error: Algorithm must be 'md5' or 'sha256'")
            return
        
        generate_hash(password, algorithm)
    
    else:
        print(f"Unknown command: {command}")
        print("Use 'crack' or 'generate'")

if __name__ == "__main__":
    main()