from agents import function_tool

@function_tool
def get_current_weather(location: str, unit: str = "fahrenheit") -> dict:
    """Get the current weather in a given location"""
    # In a real implementation, this would call a weather API.
    return {"location": location, "temperature": "72", "unit": unit, "forecast": ["sunny", "windy"]}    
