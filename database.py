from supabase import create_client
import os

SUPABASE_URL = "https://koqnqotxchpimovxcnva.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtvcW5xb3R4Y2hwaW1vdnhjbnZhIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NTE3Mzk4MCwiZXhwIjoyMDYwNzQ5OTgwfQ.bFAEslvrVDE2i7En3Ln8_AbQPtgvH_gElnrBcPBcSMc"  # Важно: service_role, не public!
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_user(user_id: int):
    res = supabase.table("users").select("*").eq("user_id", user_id).execute()
    return res.data[0] if res.data else None

def update_user(user_id: int, **kwargs):
    res = supabase.table("users").update(kwargs).eq("user_id", user_id).execute()
    return res.data[0]