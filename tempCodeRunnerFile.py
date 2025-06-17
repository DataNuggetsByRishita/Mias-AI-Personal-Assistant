def speak(self, text):
        pythoncom.CoInitialize()  # Initialize the COM library
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(f"{text}")
        pythoncom.CoUninitialize()