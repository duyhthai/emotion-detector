import unittest
from EmotionDetection.emotion_detection import emotion_detector

def get_dominant_emotion(text_to_analyze):
    emotion = emotion_detector(text_to_analyze)
    return emotion['dominant_emotion']

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        self.assertEqual(
            get_dominant_emotion('I am glad this happened'),
            'joy')
        self.assertEqual(
            get_dominant_emotion('I am really mad about this'),
            'anger')
        self.assertEqual(
            get_dominant_emotion('I feel disgusted just hearing about this'),
            'disgust')
        self.assertEqual(
            get_dominant_emotion('I am so sad about this'),
            'sadness')
        self.assertEqual(
            get_dominant_emotion('I am really afraid that this will happen'),
            'fear')
            
if __name__ == '__main__':
    unittest.main()