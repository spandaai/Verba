import asyncio
import websockets
import json
import base64
import os
from rake_nltk import Rake  # Import RAKE for keyword extraction
from RagConfigAndCredentials import credentials_default, RagConfigForGeneration  # Importing from RagConfig

# Function to extract keywords using RAKE
def extract_keywords_rake(text, max_labels=5):
    # Initialize RAKE
    rake = Rake()

    # Extract keywords from the text
    rake.extract_keywords_from_text(text)

    # Get the ranked phrases (as tuples with score and phrase)
    ranked_phrases = rake.get_ranked_phrases()

    # Limit the number of keywords to max_labels
    return ranked_phrases[:max_labels]

async def test_file_import():
    uri = "ws://localhost:8000/ws/import_files"  # WebSocket URL for the import

    # Extracting credentials and RAG config from RagConfigAndCredentials
    credentials = credentials_default["credentials"]
    rag_config = RagConfigForGeneration["rag_config"]

    file_path = "temp_file/example(7).pdf"  # Filepath you want to import

    # Get file size in bytes
    file_size = os.path.getsize(file_path)

    # Base64-encode the file content
    with open(file_path, "rb") as file:
        file_content_bytes = file.read()
        file_content_encoded = base64.b64encode(file_content_bytes).decode('utf-8')

    # You need to decode the base64 content for keyword extraction
    file_text_content = file_content_bytes.decode("utf-8", errors="ignore")

    # Extract keywords using RAKE
    keywords = extract_keywords_rake(file_text_content, max_labels=5)
    
    # Create the chunk data to be sent via WebSocket
    chunk_data = {
        "fileID": os.path.basename(file_path),
        "filename": os.path.basename(file_path),
        "extension": os.path.splitext(file_path)[1][1:],  # File extension without dot
        "status_report": {},
        "source": "",
        "isURL": False,
        "metadata": "",  # You can add more metadata here
        "overwrite": False,
        "content": file_content_encoded,  # base64-encoded content
        "labels": keywords,  # Use extracted keywords as labels
        "file_size": file_size,  # Add file size here
        "status": "READY",  # Status
        "rag_config": rag_config  # RAG config from RagConfigAndCredentials.py
    }

    # WebSocket payload with the chunk data
    payload = {
        "chunk": json.dumps(chunk_data),  # JSON string of the chunk data
        "isLastChunk": True,  # Set to True as this is a single file
        "total": 1,  # Total number of chunks (1 in this case)
        "order": 1,  # The current chunk order
        "fileID": os.path.basename(file_path),  # Unique file identifier
        "credentials": credentials  # Credentials from RagConfigAndCredentials.py
    }

    try:
        # Open WebSocket connection
        async with websockets.connect(uri) as websocket:
            # Send the payload as JSON string
            await websocket.send(json.dumps(payload))
            
            # Await and print response from the WebSocket server
            response = await websocket.recv()
            print(f"Response: {response}")

            # Keep the connection open for debugging (optional)
            await asyncio.sleep(5)  # Sleep for 5 seconds for debugging purposes
    except Exception as e:
        print(f"Error during WebSocket connection: {str(e)}")

# Run the WebSocket client
asyncio.get_event_loop().run_until_complete(test_file_import())
