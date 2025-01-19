#!/usr/bin/env python3
import random
import string
import argparse

def generate_password(length=12, use_special=True):
    """Generate a random password with specified length and complexity"""
    chars = string.ascii_letters + string.digits
    if use_special:
        chars += string.punctuation
        
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description='Generate secure random passwords')
    parser.add_argument('-l', '--length', type=int, default=None,
                       help='Password length (default: ask)')
    parser.add_argument('-s', '--simple', action='store_false',
                       help='Exclude special characters')
    parser.add_argument('-n', '--number', type=int, default=None,
                       help='Number of passwords to generate (default: ask)')
    
    args = parser.parse_args()
    
    # Get number of passwords if not provided
    if args.number is None:
        while True:
            try:
                args.number = int(input("How many passwords to generate? "))
                if args.number > 0:
                    break
                print("Please enter a positive number")
            except ValueError:
                print("Please enter a valid number")
    
    # Get password length if not provided
    if args.length is None:
        while True:
            try:
                args.length = int(input("Password length? "))
                if args.length > 0:
                    break
                print("Please enter a positive number")
            except ValueError:
                print("Please enter a valid number")
    
    # Generate and display passwords
    passwords = []
    for _ in range(args.number):
        password = generate_password(args.length, not args.simple)
        print(password)
        passwords.append(password)
    
    # Ask if user wants to save passwords
    save = input("\nDo you want to save these passwords? (yes/no): ").lower()
    if save in ['y', 'yes']:
        with open('Password.txt', 'a') as f:
            f.write("\n".join(passwords) + "\n")
        print("Passwords saved to Password.txt")

if __name__ == '__main__':
    main()
