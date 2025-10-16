import os
import sys
from server import app

def check_env_file():
    if not os.path.exists('.env'):
        print("⚠️  Warning: .env file not found!")
        print("   Copy .env.example to .env and add your API keys")
        print("   cp .env.example .env")
        return False
    return True

def main():
    print("🚀 Starting API Documentation Agent...")
    
    if not check_env_file():
        response = input("Continue anyway? (y/N): ")
        if response.lower() != 'y':
            sys.exit(1)
    
    print("📚 ATORAK: A Theory of Robust API Knowledge")
    print("🔗 Server will be available at: http://localhost:5000")
    print("💡 Use Ctrl+C to stop the server")
    print("-" * 50)
    
    # Import and run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
