import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.0 (Windows Version)")

    while True:
        x = input("Enter what you want me to speak \n")

        if x.lower() == 'q':  # Allow case-insensitive 'q' to quit
            a = "Nice to talk to you, will meet again soon"
            command = f'PowerShell -Command "Add-Type -AssemblyName System.speech; ' \
                  f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; ' \
                  f'$speak.Speak(\'{a}\');"'

            os.system(command)
            break

        # Windows PowerShell command for text-to-speech
        command = f'PowerShell -Command "Add-Type -AssemblyName System.speech; ' \
                  f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; ' \
                  f'$speak.Speak(\'{x}\');"'

        os.system(command)
