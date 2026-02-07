def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Error: template should be a string")
        return


    if len(template) == 0:
        print("Template is empty, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        content = template
        
        with open(f"output_{i}.txt", "w") as f:
            f.write(content)
