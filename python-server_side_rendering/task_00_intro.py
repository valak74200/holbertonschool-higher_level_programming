#!/usr/bin/env python3
"""
Module for generating invitation files from a template and attendee data.
"""
import os


def generate_invitations(template, attendees):
    """
    Generate invitation files for each attendee using the provided template.

    Args:
        template (str): The template string with placeholders.
        attendees (list): A list of dictionaries containing attendee information.

    Returns:
        None
    """
    # Check input types
    if not isinstance(template, str):
        print(f"Error: Template must be a string, got {type(template).__name__}")
        return

    if not isinstance(attendees, list):
        print(f"Error: Attendees must be a list, got {type(attendees).__name__}")
        return

    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Check if all items in attendees are dictionaries
    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: All attendees must be dictionaries")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, 1):
        # Create a copy of the template
        invitation = template
        
        # Replace placeholders with values from attendee dictionary
        # If a value is missing, replace with "N/A"
        placeholders = ["name", "event_title", "event_date", "event_location"]
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            # Handle None or missing values
            if value is None or value == "":
                value = "N/A"
            # Replace the placeholder with the value
            invitation = invitation.replace(f"{{{placeholder}}}", str(value))
        
        # Generate output file
        output_filename = f"output_{i}.txt"
        with open(output_filename, 'w') as file:
            file.write(invitation)
        
        print(f"Generated {output_filename}")


if __name__ == "__main__":
    # This block allows for testing the function directly
    # Read the template from a file
    try:
        with open('template.txt', 'r') as file:
            template_content = file.read()
        
        # Example attendees list
        attendees = [
            {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
            {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
            {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
        ]
        
        # Call the function
        generate_invitations(template_content, attendees)
    except FileNotFoundError:
        print("Template file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
