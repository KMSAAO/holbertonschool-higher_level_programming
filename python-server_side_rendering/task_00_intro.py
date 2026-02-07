def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template should be a string")
        return
    
    if not isinstance(attendees, list):
        print("Error: attendees should be a list")
        return

    if len(template) == 0:
        print("Template is empty, no output files generated.")
        return
    
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        content = template
        
        keys = ["name", "event_title", "event_date", "event_location"]
        
        for key in keys:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            
            placeholder = "{" + key + "}"
            content = content.replace(placeholder, str(value))
        

        with open(f"output_{i}.txt", "w") as f:
            f.write(content)
