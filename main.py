import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt 
from call_function import available_functions, call_function

def main():

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()

    # Format the user input into the structure expected by the Gemini API
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)

    success = False

    for _ in range(20):

        response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt,
            temperature=0
            )
        )

        # Ensure usage metadata is available (used for debugging/token tracking)
        if response.usage_metadata is None:
            raise RuntimeError("usage_metadata is None")
        
        if args.verbose:

            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        for candidate in response.candidates:
            messages.append(candidate.content)

        if not response.function_calls:
            print(response.text)
            success = True
            break 
        else:
            function_responses = []

            for function_call in response.function_calls:
                function_call_result = call_function(function_call, verbose=args.verbose)

                if not function_call_result.parts:
                    raise Exception("empty parts in function call result")
                
                if function_call_result.parts[0].function_response is None:
                    raise Exception("missing function_response in part")
                
                if function_call_result.parts[0].function_response.response is None:
                    raise Exception("missing response in function_response")
                
                function_responses.append(function_call_result.parts[0])

                if args.verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")

        messages.append(types.Content(role="user", parts=function_responses))
   
    if not success:
        print("Error: model did not complete the task within the iteration limit.")
        exit(1)

if __name__ == "__main__":
    main()
