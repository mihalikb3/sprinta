import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from pathlib import Path
from sprinta.models import UserProfile

PAPERS_DIR = Path("papers")
STORAGE_DIR = Path("storage")

def initialize_ai():
    """Initialize the RAG index from the papers directory."""
    if not PAPERS_DIR.exists():
        PAPERS_DIR.mkdir(parents=True)
    
    # Check if storage already exists
    if STORAGE_DIR.exists():
        storage_context = StorageContext.from_defaults(persist_dir=str(STORAGE_DIR))
        index = load_index_from_storage(storage_context)
    else:
        # Load papers and create index
        documents = SimpleDirectoryReader(str(PAPERS_DIR)).load_data()
        if not documents:
            # Create a dummy index if no papers yet
            from llama_index.core.schema import Document
            documents = [Document(text="Running science basics: Consistency is key.")]
        
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=str(STORAGE_DIR))
    
    return index

def generate_workout(profile: UserProfile):
    """Generate a workout recommendation based on scientific principles and user profile."""
    index = initialize_ai()
    query_engine = index.as_query_engine()
    
    prompt = f"""
    Based on the scientific research papers available, recommend a running workout for a user with the following profile:
    - Name: {profile.name}
    - Race Goal: {profile.race_goal}
    - Weekly Mileage Target: {profile.weekly_mileage_target} km
    - Strength Training Included: {profile.weights_included}
    
    Please provide a specific workout description including warm-up, main set, and cool-down.
    """
    
    response = query_engine.query(prompt)
    return str(response)
