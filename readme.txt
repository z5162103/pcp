HOW TO EXECUTE THE PROJECT
To execute the project, run 'python keylog.py' and 'python screenshot.py' in two separate terminals
You may need to install dependencies like pynput, pyautogui
To install this, use 'pip install pynput' and 'pip install pyautogui'


TROUBLESHOOTING
"raise exceptions.RefreshError(error_details, response_data)
google.auth.exceptions.RefreshError: ('invalid_grant: Token has been expired or 
revoked.', {'error': 'invalid_grant', 'error_description': 'Token has been expired or revoked.'})"

If there are any issues with the Google Drive tokens (expired tokens) follow the steps here:
1. Login the Gmail account timothytestyeo@gmail.com
2. Delete token_drive_v3.pickle
3. Run 'python keylog.py'
4. Follow prompts to authorise the Gmail account timothytestyeo@gmail.com

Login for the Google Drive can be found in the report.
The token will expire every week or so.

If there are any other issues, please email my student email.


