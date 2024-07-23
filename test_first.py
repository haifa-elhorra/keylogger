import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
import logging
from pynput.keyboard import Key

# Define the functions and configurations to be tested
log_dir = r"C:/Users/Haifa Elhorra/Desktop/projet/keyylogger"

def create_log_dir():
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

def configure_logging():
    logging.basicConfig(filename=os.path.join(log_dir, "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

class TestKeylogger(unittest.TestCase):

    @patch('os.makedirs')
    @patch('os.path.exists', return_value=False)
    def test_directory_creation(self, mock_exists, mock_makedirs):
        create_log_dir()
        mock_exists.assert_called_with(log_dir)
        mock_makedirs.assert_called_with(log_dir)

    @patch('logging.basicConfig')
    def test_logging_configuration(self, mock_basicConfig):
        configure_logging()
        mock_basicConfig.assert_called_with(
            filename=os.path.join(log_dir, "keyLog.txt"),
            level=logging.DEBUG,
            format='%(asctime)s: %(message)s'
        )

    @patch('logging.info')
    def test_on_press(self, mock_logging_info):
        key = 'a'
        on_press(key)
        mock_logging_info.assert_called_with("'a'")

    @patch('pynput.keyboard.Listener')
    def test_listener(self, mock_listener):
        listener_instance = mock_listener.return_value
        with patch('builtins.__import__', side_effect=ImportError):
            with patch('pynput.keyboard.Listener') as mock_listener:
                listener_instance = mock_listener.return_value
                listener_instance.__enter__.return_value = listener_instance
                listener_instance.__exit__.return_value = False
                with listener_instance:
                    listener_instance.join()
                mock_listener.assert_called_with(on_press=on_press)
                listener_instance.join.assert_called()

if __name__ == '__main__':
    unittest.main()
