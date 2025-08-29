# generate_welcome.py
# Usage: python scripts/generate_welcome.py "Name" "email@example.com" "ProductName" "Role"
# This script calls OpenAI to create a 3 step onboarding sequence and then prints it.

import os
import sys
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate(name, email, product, role):
    prompt = (
        f"You are a helpful onboarding content writer. Create a friendly 3-step onboarding plan for {name} "
        f"who just signed up for {product}. Their role is {role}. Keep steps short and actionable, each with a 1-line description."
    )
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.2
    )
    return resp["choices"][0]["message"]["content"].strip()

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python generate_welcome.py Name email product role")
        sys.exit(1)
    name, email, product, role = sys.argv[1:5]
    print("--- Generating welcome sequence ---")
    print(generate(name, email, product, role))
