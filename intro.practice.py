import pandas as pd
import numpy as np

# Variables
pulse_rate_variable = 70
string_variable = "Pulse Rate Review"
list_variable = ["Normal", "Tachycardia", "Bradycardia"]
dictionary_variable = {
    "category": "Pulse Rate",
    "normal_range": "60-100 bpm",
    "pulse_rate": pulse_rate_variable,
    "pulse_rate_conditions": {
        "Normal": "Pulse rate is within normal limits (60-100 bpm)",
        "Tachycardia": "Pulse rate is above limits (greater than 100 bpm).",
        "Bradycardia": "Pulse rate is below limits (less than 60 bpm)."
    },
    "health_factors_affecting_pulse_rate": {
        "medication_regimen": "some medications may increase or decrease pulse rate",
        "physical_activity": "pulse rate is affected by level of activity",
        "internal_factors": "stress, exhaustion, and anxiety may affect pulse rate",
    } 
}

# Function to analyze pulse rate
def analyze_pulse_rate(pulse_rate):
    """
    Analyzes pulse rate and returns a message denoting its category.
    
    :param pulse_rate: Pulse rate in beats per minute (bpm)
    :return: A string message indicating the pulse rate category
    """
    if pulse_rate < 60:
        return "Bradycardia: Pulse rate is below normal limits."
    elif 60 <= pulse_rate <= 100:
        return "Normal: Pulse rate is within normal limits."
    else:
        return "Tachycardia: Pulse rate is above normal limits."

# Print statements
print("Pulse Rate Variable (bpm):", pulse_rate_variable)
print("String Variable:", string_variable)
print("List Variable (Pulse Rate Categories):", list_variable)
print("Dictionary Variable (Pulse Rate Info):", dictionary_variable)

# Run function and print result
pulse_rate_result = analyze_pulse_rate(pulse_rate_variable)
print("Pulse Rate Analysis:", pulse_rate_result)
