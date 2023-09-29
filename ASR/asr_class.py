import whisper

class ASR():

    def __init__(self):

        self.model = whisper.load_model("large")
        self.script = ''

    def run_ASR(self, s):

        self.script = self.model.transcribe(s)['text']

        return self.script
