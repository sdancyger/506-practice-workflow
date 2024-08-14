# 506-practice-workflow
Primer assignment for SBU MS AHI 504/507 Fall semester classes to practice a basic development workflow 

# 506-practice-workflow
Primer assignment for SBU MS AHI 504/507 Fall semester classes to practice a basic development workflow


# Summary of variables
The variabes I created relate to pulse rate readings.

~ pulse_rate_variable = 70
    Relates to the standard pulse rate variable reading of 70.

~ string_variable = "Pulse Rate Review"
    This is the title to specify the chosen topic for this assignment.

~ list_variable = ["Normal", "Tachycardia", "Bradycardia"]
    This indicates the different categories that certain pulse rates will be categorized under.

~ dictionary_variables includes three subcategories: 
    "category", "normal_range", "pulse_rate", and "pulse_rate_conditions". "Pulse_rate_conditions" is also a nested dictionary that addresses three descriptions for different pulse rates. The nested dictionary list includes: what a "normal" pulse rate range is (60-100bpm), a "tachycardic" pulse rate (>100bpm), and a "bradycardic" pulse rate (<60bpm).

~ health_factors_affecting_pulse_rate, is another nested        
    dictionary variable that consists of three other subcategories. The nested dictionary variables include three health factors that affect one's pulse rate, which are: "medication_regimen", "physical_activity", and "internal_factors".

# Explanation of the function
The function def, analyze_pulse_rate(pulse_rate): , is aimed to analyze the pulse rates and categorize them into either "normal"(60-100bpm), "tachycardia"(>100bpm), or "bradycardia"(<60bpm>). The parameter is indicated by, :param pulse_rate:, and will be the pulse rate(bpm) inputted. It is followed by the, :return: , which will output a string message result with the correct pulse rate category. The statements, 'if', 'elif', and 'else' follow , which allows for the categorization of the pulse rate numerical.


# Expected output based on inputted data
The expected output based on the inputted data includes a categorization of all inputted pulse rates into the three categorical options: normal, tachycardia, and bradycardia. For example, if a pulse rate of 88bpm was inputted into the function, it would be analyzed and would relay the output of "normal", due to the normal pulse rate range being from 60-100bpm.

