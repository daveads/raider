import datetime

async def generate_html_table(lead_data, users_daily=None):
    current_date = datetime.datetime.now()  # Get the current date and time
    current_date_str = current_date.strftime("%d-%m-%Y") 
    
    # Generate html table
    html_table = "<table>"
    html_table += f"<thead><tr><th>Username</th><th>Name</th><th>Total_Commit {current_date_str}</th></tr></thead>"
    html_table += "<tbody>"
    
    for i, row in enumerate(lead_data, start=1):  # Add enumerate to get the index (start=1 to start numbering from 1)
        # Access individual elements of each list (username, name, and contributions)
        username = f"{i}.   {row[0]}"  # Add number to the username
        name = row[1]
        contributions = row[2]

        html_table += f"<tr><td>{username}</td><td>{name}</td><td>{contributions}</td></tr>"
    
    html_table += "</tbody></table><br><br>"
    
    html_table += "<strong>DAILY COMMITS</strong>"

    if users_daily:
        sorted_user_dict = dict(sorted(users_daily.items(), key=lambda item: int(item[1]), reverse=True))

        for username, commits in sorted_user_dict.items():
            html_table += f"<p><strong>{str(username).capitalize()}</strong> COMMITS FOR THE DAY : <strong>{commits}</strong> </p>"
        
    # HTML template
    html_template = """
    <html>
        <head>
            <style>
                table {
                    border-collapse: collapse;
                    width: 50%;
                }
                
                th, td {
                    text-align: left;
                    padding: 8px;
                }
                
                th {
                    background-color: #f2f2f2;
                }
            </style>
        </head>
        <body>
            {{TABLE}}
        </body>
    </html>
    """

    html_page = html_template.replace("{{TABLE}}", html_table)
    return html_page
